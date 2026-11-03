+++
kind  = "proof"
of    = "lemma-nagata-intermediate-separated"
uses = ["def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-two-open-boundary-loci", "lemma-nagata-boundary-loci", "lemma-nagata-intermediate-overlap-closed", "lemma-nagata-intermediate-overlap-constructible", "lemma-nagata-intermediate-overlap-specialization-closed", "lemma-nagata-intermediate-specialization-boundary", "lemma-nagata-separated-two-open-cover"]
+++
The opens $U$ and $X_i\setminus\overline Z_{i,j}$ cover $W_i$. The first
is separated and of finite type over $S$ by the section hypotheses. The
second has those properties because it is open in the proper scheme
$X_i\to S$. Their overlap map is the closed immersion supplied by
[lemma-nagata-intermediate-overlap-closed]. Apply
[lemma-nagata-separated-two-open-cover] to these two opens to obtain
separatedness of $W_i\to S$. Being locally of finite type is local on
the source, so $W_i\to S$ is locally of finite type. The open $U$ is
quasi-compact, since $U\to S$ is quasi-compact and $S$ is quasi-compact.
The scheme $X_i$ is of finite type over the Noetherian scheme $S$, hence
Noetherian, so its open subscheme $X_i\setminus\overline Z_{i,j}$ is
quasi-compact. Thus $W_i$, covered by these two opens, is quasi-compact.
As $S$ is Noetherian, hence quasi-separated, $W_i\to S$ is quasi-compact,
and so of finite type.
