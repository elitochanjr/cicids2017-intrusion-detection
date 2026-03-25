# Data

Raw and processed data files are not tracked in this repository due to file size.

## Dataset: CICIDS2017

**Source:** Canadian Institute for Cybersecurity, University of New Brunswick
**Official page:** https://www.unb.ca/cic/datasets/ids-2017.html
**Kaggle mirror:** https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset

### Download instructions

**Option A — Kaggle CLI:**
```bash
kaggle datasets download -d chethuhn/network-intrusion-dataset
unzip network-intrusion-dataset.zip -d data/raw/
```

**Option B — Manual:**
Download the ZIP from Kaggle and extract the CSV files into `data/raw/`.

### Expected structure after download

```
data/
├── raw/
│   ├── Monday-WorkingHours.pcap_ISCX.csv
│   ├── Tuesday-WorkingHours.pcap_ISCX.csv
│   ├── Wednesday-workingHours.pcap_ISCX.csv
│   ├── Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
│   ├── Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
│   ├── Friday-WorkingHours-Morning.pcap_ISCX.csv
│   ├── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
│   └── Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
└── README.md
```

### Kaggle credentials

Place your `kaggle.json` credentials file at `~/.kaggle/kaggle.json` (Linux/Mac) or `%USERPROFILE%\.kaggle\kaggle.json` (Windows). Never commit this file to the repository.
