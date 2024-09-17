# Sentinel2Video

This is a simple tool to convert images from sentinel 2 satellite to video.

## Installation

Clone the repository and use `pip install .` to install the script.
Alternatively you can use following commands to install 
dependencies in a virtual environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

After that use `python3 ./sentinel2video` to execute the script.

## Usage

### Synopsis

**sentinel2video** [-h | --help]

**sentinel2video** --start START
                   --end END
                   [--project PROJECT]
                   [--fps FPS]
                   [--bands BANDS [BANDS ...]]
                   [--gamma GAMMA [GAMMA ...]]
                   [--min MIN [MIN ...]]
                   [--max MAX [MAX ...]]
                   [--output OUTPUT]
                   [--scale SCALE]
                   [--tiles TILES [TILES ...]]
                   [--polling POLLING]

### Options

* **-h**, **--help**  
  Show help message and exit.
* **--start START**  
  Start date of the video.
* **--end END**  
  End date of the video.
* **--project PROJECT**  
  Project name on google cloud. Defaults to **sentinel2video**.
* **--fps FPS**  
  Framerate of the video. Defaults to **1**.
* **--bands BANDS [BANDS ...]**  
  Spectral bands. Defaults to **B4 B3 B2**.
* **--gamma GAMMA [GAMMA ...]**  
  Gamma(s) for each band. Defaults to **0.95 1.0 1.0**.
* **--min MIN [MIN ...]**  
  Value(s) to map to 0 for each band. Defaults to **0.0 0.0 0.0**.
* **--max MAX [MAX ...]**  
  Value(s) to map to 255 for each band. Defaults to **3000.0 3000.0 3000.0**.
* **--min-cloud MIN_CLOUD**  
  Minimum cloud pixel percantage. Defaults to **0.0**.
* **--max-cloud MAX_CLOUD**  
  Maximum cloud pixel percantage. Defaults to **100.0**.
* **--min-coverage MIN_COVERAGE**  
  Minimum cloud coverage assessment. Defaults to **0.0**.
* **--max-coverage MAX_COVERAGE**  
  Maximum cloud coverage assessment. Defaults to **100.0**.
* **--min-water MIN_WATER**  
  Maximum water pixel percantage. Defaults to **0.0**.
* **--max-water MAX_WATER**  
  Maximum water pixel percantage. Defaults to **100.0**.
* **--output OUTPUT**  
  Output filename of rendered video. Defaults to **out**.
* **--scale SCALE**  
  Scale. Defaults to **100**.
* **--tiles TILES [TILES ...]**  
  US-Military Grid Reference System (MGRS) tile(s). Defaults to **31UET**.
* **--polling POLLING**  
  Polling interval in seconds. Defaults to **5**.
