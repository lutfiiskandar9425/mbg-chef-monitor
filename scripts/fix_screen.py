import os

path = r'mbg_chef_monitor/lib/screens/home_screen.dart'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add _formatIndonesianDate helper
helper = '''  String _formatIndonesianDate(DateTime date) {
    const days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'];
    const months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'];
    final dayName = days[(date.weekday - 1).clamp(0, 6)];
    final monthName = months[date.month.clamp(1, 12)];
    return '$dayName, ${date.day} $monthName ${date.year}';
  }

  @override
  Widget build(BuildContext context) {'''

if '_formatIndonesianDate' not in c:
    c = c.replace('  @override\n  Widget build(BuildContext context) {', helper, 1)

# 2. Add errorBuilder to Image.asset
old_img = '''          child: Image.asset(
            'assets/images/bgn_logo.png',
            fit: BoxFit.contain,
          ),'''

new_img = '''          child: Image.asset(
            'assets/images/bgn_logo.png',
            fit: BoxFit.contain,
            errorBuilder: (_, __, ___) => Container(
              decoration: const BoxDecoration(
                color: Color(0xFF0F172A),
                shape: BoxShape.circle,
              ),
              alignment: Alignment.center,
              child: const Text('BGN', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 10)),
            ),
          ),'''

c = c.replace(old_img, new_img, 1)

# 3. Replace DateFormat('EEEE, dd MMM yyyy', 'id_ID').format(_selectedDate)
old_date = "DateFormat('EEEE, dd MMM yyyy', 'id_ID').format(_selectedDate)"
new_date = "_formatIndonesianDate(_selectedDate)"
c = c.replace(old_date, new_date, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print('fix_screen.py executed successfully!')

