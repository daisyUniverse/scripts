inotifywait -m -r $@ -e create |
    while read path action file; do
        if [[ "$file" =~ .*m4v$ ]]; then
            python notify.py "$file" | discho -c movie-rips 
        fi
    done
