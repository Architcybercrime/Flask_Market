 (Join-Path $lessonDir 'seed_demo.py')

Write-Host 'Starting Flask app...'
python (Join-Path $lessonDir 'run.py')
