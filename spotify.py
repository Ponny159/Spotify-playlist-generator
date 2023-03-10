import argparse
import csv
import random

def generate_playlist(history_file, num_songs, mode):
  with open(history_file, 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    next(reader)
    songs = [(row[6], row[2]) for row in reader]

  song_counts = {}
  artist_dict = {}
  for song, artist in songs:
    song_counts[song] = song_counts.get(song, 0) + 1
    artist_dict[song] = artist

  sorted_songs = sorted(song_counts.items(), key=lambda x: x[1], reverse=True)
  playlist = [f"{artist_dict[song]} – {song} ({playcount})" for song, playcount in (sorted_songs[:num_songs] if mode == 'top' else random.sample(sorted_songs, num_songs))]
  
  return playlist

def main():
  parser = argparse.ArgumentParser(description='Spotify playlist generator.', prog='spotify.py')
  parser.add_argument('-t', '--type', choices=['top', 'random'], required=False, help='Choose "top" for playlist with the most plays or "random" for playlist with random songs.')
  parser.add_argument('-s', '--songs', type=int, required=False, help='Number of songs in the generated playlist.')
  parser.add_argument('file', help='Input CSV file name.')
  args = parser.parse_args()

  playlist = generate_playlist(args.file, args.songs, args.type)

  for song in playlist:
    print(song)

if __name__ == '__main__':
  main()
