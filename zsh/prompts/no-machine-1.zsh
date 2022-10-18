status_bad_F=163
status_bad_K=231
user_color=080
pdir_color=075
other_color=186

prev_status="%(?..%K{$status_bad_K}%F{$status_bad_F}bad%f%k )"
user="%F{$user_color}%n%f"
at="%F{$other_color}@%f"
coln="%F{$other_color}:%f"
pdir="%F{$pdir_color}%3~%f"
arrow="%F{$other_color}>%f"

PROMPT="$prev_status$user$coln$coln$pdir$arrow "
