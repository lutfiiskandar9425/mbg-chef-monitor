import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import pkcs12, BestAvailableEncryption
import os

key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "ID"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Jawa Tengah"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Pekalongan"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Yayasan Maranatha"),
    x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, "SPPG MBG"),
    x509.NameAttribute(NameOID.COMMON_NAME, "MBG Chef Monitor"),
])

now = datetime.datetime.now(datetime.timezone.utc)
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(now - datetime.timedelta(days=1))
    .not_valid_after(now + datetime.timedelta(days=3650)) # 10 years validity
    .add_extension(
        x509.BasicConstraints(ca=False, path_length=None), critical=True
    )
    .sign(key, hashes.SHA256())
)

password = b"mbgsecret2026"
p12_data = pkcs12.serialize_key_and_certificates(
    name=b"mbgkey",
    key=key,
    cert=cert,
    cas=None,
    encryption_algorithm=BestAvailableEncryption(password),
)

out_path = r"C:\Users\HP\Projects\APlikasi MBG\mbg_chef_monitor\android\app\upload-keystore.p12"
with open(out_path, "wb") as f:
    f.write(p12_data)

print(f"Generated permanent keystore: {out_path} ({len(p12_data)} bytes)")

