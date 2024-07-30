#!/usr/bin/env python3

import argparse
import ee
import time

if __name__ == '__main__':
  parser = argparse.ArgumentParser(prog='sentinel2video',
                                  description='Turn sentinel 2 satellite images to video.')

  parser.add_argument('--start', help='Start date of the video.', type=str, required=True)
  parser.add_argument('--end', help='End date of the video.', type=str, required=True)
  parser.add_argument('--project', help='Project name on google cloud.', type=str, default='sentinel2video')
  parser.add_argument('--fps', help='Framerate of the video.', type=int, default=1)
  parser.add_argument('--bands', help='Spectral bands.', nargs='+', default=['B4', 'B3', 'B2'])
  parser.add_argument('--gamma', help='Gamma(s) for each band.', nargs='+', default=[0.95, 1.0, 1.0])
  parser.add_argument('--min', help='Value(s) to map to 0 for each band.', nargs='+', default=[0.0, 0.0, 0.0])
  parser.add_argument('--max', help='Value(s) to map to 255 for each band.', nargs='+', default=[3000.0, 3000.0, 3000.0])
  parser.add_argument('--output', help='Output filename of rendered video.', type=str, default='out')
  parser.add_argument('--scale', help='Scale.', type=int, default=100)
  parser.add_argument('--tiles', help='US-Military Grid Reference System (MGRS) tile(s)', nargs='+', default=['31UET'])
  parser.add_argument('--polling', help='Polling interval in seconds.', type=int, default=5)

  args = parser.parse_args()

  # Authenticate to google earth engine
  ee.Authenticate()

  # Select project
  ee.Initialize(project=args.project)

  dataset = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
              .filter(ee.Filter.inList('MGRS_TILE', args.tiles)) \
              .filterDate(args.start, args.end) \
              .map(lambda image: image.visualize(bands=args.bands,
                                                 gamma=args.gamma,
                                                 min=args.min,
                                                 max=args.max))

  task = ee.batch.Export.video.toDrive(
      collection=dataset,
      framesPerSecond=args.fps,
      description=args.output,
      scale=args.scale
  )
  task.start()

  while task.active():
    print('Pending task with id: {}'.format(task.id))
    time.sleep(args.polling)

