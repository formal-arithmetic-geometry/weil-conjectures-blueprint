+++
kind  = "proof"
of    = "sk-lem-nagata-sketch-elimination"
uses = ["thm-nagata-conrad-elimination"]
+++
First blow up a finite-type ideal supported exactly on $T\setminus U$, so
that $U$ becomes scheme-theoretically dense
([sk-lem-nagata-boundary-divisor]). Apply [thm-nagata-conrad-elimination] with
$V=U$ to the section $U\to W$ inverse to $W_U\to U$. Refine once more by a
product with an ideal cutting out $T\setminus U$, and compose the blow-ups
into one $U$-admissible blow-up $T'\to T$ ([sk-lem-nagata-sketch-blowups]).
The extended section is defined on an open $W_0\subseteq T'$ and has closed
graph $\Gamma\simeq W_0$ in $W\times_TT'$, containing the graph over $U$
schematically densely. The strict transform $W'$ is the scheme-theoretic
closure of that graph, so $W'=\Gamma\simeq W_0$, and $W'\to T'$ is an open
immersion.
