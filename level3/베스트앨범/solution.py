def solution(genres, plays):
    genre_dict = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in genre_dict:
            genre_dict[genre] = {'total': 0, 'songs': []}
        
        genre_dict[genre]['total'] += play
        genre_dict[genre]['songs'].append((i, play))
    
    sorted_genres = sorted(genre_dict.items(), key=lambda x: x[1]['total'], reverse=True)
    
    answer = []

    for genre, info in sorted_genres:
        songs = sorted(info['songs'], key=lambda x: (-x[1], x[0]))
        
        for i in range(min(2, len(songs))):
            answer.append(songs[i][0])
    
    return answer