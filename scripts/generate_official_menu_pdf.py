import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

def build_pdf(filename="SOP_Menu_Mingguan_SPPG_Pekajangan04.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#0F172A'),
        alignment=1 # Center
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#475569'),
        alignment=1 # Center
    )
    
    h1_style = ParagraphStyle(
        'H1Style',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=10,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'H2Style',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#059669'),
        spaceBefore=6,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#334155')
    )
    
    bold_cell = ParagraphStyle(
        'BoldCell',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0F172A')
    )

    story = []

    # 1. HEADER KOP RESMI
    story.append(Paragraph("BADAN GIZI NASIONAL (BGN) REPUBLIK INDONESIA", subtitle_style))
    story.append(Paragraph("PROGRAM MAKAN BERGIZI GRATIS (MBG) - SPPG PEKALONGAN", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("STANDAR OPERASIONAL PROSEDUR & SIKLUS MENU MINGGUAN", title_style))
    story.append(Paragraph("SPPG Kedungwuni Pekajangan 4 • Yayasan Maranatha Cita Kasih", subtitle_style))
    story.append(Paragraph("Periode: Siklus 5 Hari Kerja (Senin - Jumat) • Target: 3.000 Porsi / Hari", subtitle_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

    # 2. PANDUAN RINGKAS 3 TIM INTI
    story.append(Paragraph("DISTRIBUSI TUGAS 3 TIM INTI PRODUKSI DAPUR MBG", h1_style))
    
    summary_data = [
        [
            Paragraph("<b>TIM PERSIAPAN</b>", bold_cell),
            Paragraph("Fokus pada penerimaan bahan segar, sortir kualitas grade A, standar pengupasan (tebal/tipis), pemotongan presisi (cm) seragam, penimbangan awal bruto/tara, dan pencucian 3 tahap air mengalir.", body_style)
        ],
        [
            Paragraph("<b>TIM PENGOLAHAN</b>", bold_cell),
            Paragraph("Fokus pada proses memasak, waktu marinasi bumbu, standar suhu api, teknik pengolahan (rebus/tumis/panggang/ungkep), dan memastikan suhu inti masakan minimal 75°C sebelum diangkat.", body_style)
        ],
        [
            Paragraph("<b>TIM PEMORSIAN</b>", bold_cell),
            Paragraph("Fokus pada penataan ompreng/lunchbox, gramatur porsi matang per sekat (ditimbang berkala), menjaga suhu saji hangat minimal 60°C, serta penanganan khusus buah segar (cuci lap higienis, potong porsi dingin 80 gr).", body_style)
        ]
    ]
    
    summary_table = Table(summary_data, colWidths=[4*cm, 14*cm])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 14))

    # 3. DETAIL MENU 5 HARI (SENIN - JUMAT)
    days_data = [
        {
            "day": "SENIN",
            "menu": "Nasi Putih + Semur Ayam Fillet + Tempe Bacem + Sop Sayur + Pisang Cavendish",
            "gizi": "Energi: 685 kkal • Protein: 28 gr • Zat Besi & Serat Tinggi",
            "items": [
                ["Daging Ayam Fillet (Prohe)", "Potong dadu 2.5 x 2.5 cm rapi, buang lemak tebal, pakai keranjang hijau higienis.", "Marinasi 30 mnt kecap jahe, masak suhu inti minimal 75°C empuk meresap.", "Timbang netto 65 gr di sekat utama, jangan biarkan kuah meluber."],
                ["Wortel & Buncis Sop (Sayur)", "Wortel potong koin 0.5 cm, buncis serong 2 cm, cuci bilas air mengalir 3x.", "Rebus renyah gurih al-dente, masukkan seledri saat api hendak mati.", "Sajikan hangat min 60°C, 1 centong sayur sop merata di sekat sayur."],
                ["Tempe Kedelai (Prona)", "Potong dadu 1.5 cm rapi, susun di baki stainless berlubang tiris.", "Ungkep bumbu bacem legit gula kelapa asli hingga karamel meresap.", "1 potong bacem 40 gr di sekat ketiga ompreng."],
                ["Pisang Cavendish (Buah)", "Bantu penerimaan & sortir buah mulus grade A di area buah.", "- (Buah segar tanpa pengolahan panas)", "Lap bersih kering higienis, letakkan 1 buah utuh di sekat buah ompreng."]
            ]
        },
        {
            "day": "SELASA",
            "menu": "Nasi Putih + Daging Sapi Teriyaki + Tahu Bakso + Capcay Komplit + Jeruk Manis",
            "gizi": "Energi: 710 kkal • Protein: 31 gr • Zat Besi Heme Tinggi",
            "items": [
                ["Daging Sapi Has Luar (Prohe)", "Iris tipis memotong serat tebal 3 mm, pastikan bebas urat keras.", "Tumis saus teriyaki gurih manis, pastikan matang sempurna suhu inti 75°C.", "Timbang porsi 60 gr daging bersaus di sekat utama."],
                ["Sayur Capcay (Sayur)", "Rendam kembang kol di air garam 10 mnt, potong kuntum kecil, wortel kembang.", "Tumis cepat api besar (wok hei) agar sayuran tetap hijau segar dan renyah.", "1 centong capcay hangat di sekat sayur, kuah tidak meluber."],
                ["Tahu Bakso Sapi (Prona)", "Isi adonan bakso ke tahu pong goreng, rapikan pinggiran.", "Kukus hangat suhu inti 75°C selama 25 menit hingga matang kenyal.", "1 pcs tahu bakso utuh 45 gr di sekat pendamping."],
                ["Jeruk Manis (Buah)", "Sortir buah manis segar mulus di area buah.", "- (Buah segar tanpa pengolahan panas)", "Cuci lap kering, sajikan 1 buah jeruk manis utuh di sekat buah ompreng."]
            ]
        },
        {
            "day": "RABU",
            "menu": "Nasi Putih + Ikan Kembung Asam Manis + Tempe Mendoan + Sayur Bayam + Semangka",
            "gizi": "Energi: 660 kkal • Protein: 26 gr • Tinggi Asam Lemak Omega-3",
            "items": [
                ["Ikan Kembung Fillet (Prohe)", "QC raba pastikan bebas duri, lumuri perasan jeruk nipis 15 mnt bilas tiris.", "Goreng krispi suhu minyak 170°C, siram saus asam manis nanas sesaat sblm saji.", "1 potong 65 gr renyah di sekat lauk utama."],
                ["Bayam Hijau & Jagung (Sayur)", "Petik daun bayam segar, pipil jagung manis, bilas 3x air mengalir.", "Masak bening tidak lebih dari 3 menit agar zat besi tidak rusak.", "1 centong bening bayam jagung segar suhu min 60°C."],
                ["Tempe Mendoan (Prona)", "Iris tempe tipis 4 mm, siapkan adonan tepung terigu daun bawang.", "Goreng setengah matang (mendoan hangat) dalam minyak panas bersih.", "1 lembar tempe mendoan gurih di sekat pendamping."],
                ["Semangka Merah (Buah)", "Bantu penerimaan & cuci kulit luar semangka utuh.", "- (Buah segar tanpa pengolahan panas)", "Kupas kulit hijau, potong segitiga porsi 80 gr tanpa biji, simpan dingin."]
            ]
        },
        {
            "day": "KAMIS",
            "menu": "Nasi Putih + Ayam Panggang Madu + Rolade Tahu + Tumis Labu Siam + Melon",
            "gizi": "Energi: 690 kkal • Protein: 29 gr • Vitamin A & Kalium Optimal",
            "items": [
                ["Paha Ayam Fillet (Prohe)", "Potong porsi 70 gr, tusuk garpu agar bumbu madu meresap.", "Ungkep bumbu kuning madu, panggang oven hingga karamelisasi gurih.", "1 potong ayam panggang 70 gr mengkilap di sekat utama."],
                ["Labu Siam Muda (Sayur)", "Kupas, remas garam buang getah lengket, bilas air potong korek api 3 cm.", "Tumis bawang merah putih cabai merah iris tipis hingga harum renyah.", "1 centong tumis labu siam hangat."],
                ["Rolade Tahu Telur (Prona)", "Hancurkan tahu sutra, campur telur & wortel parut, gulung daun pisang.", "Kukus 20 menit, potong bulat tebal 1.5 cm, goreng keemasan.", "2 potong rolade tahu di sekat pendamping."],
                ["Melon Madu (Buah)", "Bantu penerimaan & bilas kulit luar melon.", "- (Buah segar tanpa pengolahan panas)", "Kupas tebal, buang biji, potong porsi 80 gr seragam, simpan dingin tertutup."]
            ]
        },
        {
            "day": "JUMAT",
            "menu": "Nasi Gurih Pandan + Telur Balado Manis + Perkedel Kentang + Lodeh Labu + Pepaya",
            "gizi": "Energi: 675 kkal • Protein: 25 gr • Serat & Beta-Karoten Tinggi",
            "items": [
                ["Telur Ayam Ras (Prohe)", "Rebus 12 menit, rendam air es, kupas kulit mulus tanpa cacat.", "Goreng berkulit tipis, lumuri bumbu balado tomat manis (standar anak SD).", "1 butir telur balado utuh di sekat utama."],
                ["Sayur Lodeh Labu (Sayur)", "Potong dadu labu jipang 2 cm, potong kacang panjang 3 cm, cuci bilas.", "Rebus santan encer segar dengan bumbu lodeh gurih aromatik tidak pedas.", "1 centong sayur lodeh hangat di sekat sayur."],
                ["Perkedel Kentang (Prona)", "Kupas kentang, potong tebal, goreng hingga empuk dan haluskan selagi hangat.", "Campur daun seledri & bawang goreng, celup kocokan telur, goreng keemasan.", "1 butir perkedel kentang padat 40 gr di sekat pendamping."],
                ["Pepaya Manis (Buah)", "Bantu penerimaan & sortir pepaya matang pohon.", "- (Buah segar tanpa pengolahan panas)", "Kupas tebal, buang biji hitam, potong dadu 3 cm porsi 80 gr, simpan dingin."]
            ]
        }
    ]

    for d in days_data:
        story.append(Paragraph(f"MENU HARI {d['day']}: {d['menu']}", h2_style))
        story.append(Paragraph(f"Kandungan Gizi: {d['gizi']}", subtitle_style))
        story.append(Spacer(1, 4))
        
        table_rows = [
            [
                Paragraph("<b>Komponen Bahan</b>", bold_cell),
                Paragraph("<b>1. Arahan Tim Persiapan</b>", bold_cell),
                Paragraph("<b>2. Arahan Tim Pengolahan</b>", bold_cell),
                Paragraph("<b>3. Arahan Tim Pemorsian</b>", bold_cell)
            ]
        ]
        
        for item in d['items']:
            table_rows.append([
                Paragraph(f"<b>{item[0]}</b>", body_style),
                Paragraph(item[1], body_style),
                Paragraph(item[2], body_style),
                Paragraph(item[3], body_style)
            ])
            
        menu_table = Table(table_rows, colWidths=[3.8*cm, 4.8*cm, 4.8*cm, 4.6*cm])
        menu_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ]))
        story.append(menu_table)
        story.append(Spacer(1, 10))

    # 4. LEMBAR TANDA TANGAN RESMI
    story.append(Spacer(1, 15))
    sign_data = [
        [
            Paragraph("Disusun & Ditetapkan Oleh:<br/><b>Head Chef SPPG Pekajangan 4</b><br/><br/><br/><br/><b><u>Chef Lutfi Iskandar</u></b><br/>Penanggung Jawab Dapur Produksi", body_style),
            Paragraph("Diverifikasi Standar Gizi Oleh:<br/><b>Tim Ahli Gizi / Nutritionist BGN</b><br/><br/><br/><br/><b><u>Ahli Gizi SPPG Pekajangan 4</u></b><br/>Yayasan Maranatha Cita Kasih", body_style),
            Paragraph("Mengetahui & Menyetujui:<br/><b>Kepala Satuan Pelayanan (SPPG)</b><br/><br/><br/><br/><b><u>Pimpinan SPPG Kedungwuni 4</u></b><br/>Program MBG BGN RI", body_style)
        ]
    ]
    sign_table = Table(sign_data, colWidths=[6*cm, 6*cm, 6*cm])
    sign_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(sign_table)

    doc.build(story)
    print(f"Successfully generated official PDF: {filename}")

if __name__ == '__main__':
    build_pdf()

