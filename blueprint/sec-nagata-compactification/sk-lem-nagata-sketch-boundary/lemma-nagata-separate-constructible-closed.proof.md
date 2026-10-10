+++
kind  = "proof"
of    = "lemma-nagata-separate-constructible-closed"
uses = ["def-nagata-constructible-closed-support", "def-nagata-extended-ideal", "def-nagata-finite-type-ideal-extension", "def-nagata-qc-open-complement-ideal", "def-nagata-scheme-image-factor", "def-nagata-separate-closed-subschemes", "def-nagata-strict-transform", "lemma-nagata-constructible-closed-support", "lemma-nagata-extend-finite-type-ideal", "lemma-nagata-qc-open-complement-ideal", "lemma-nagata-qc-open-complement-ideal-exists", "lemma-nagata-separate-closed-subschemes", "lemma-nagata-strict-transform-closure-characterization"]
+++
Let $\mathcal J_i$, $\mathcal I_i$ and $Z_i=V(\mathcal I_i)$ be as in
[def-nagata-separate-constructible-closed], so that the $\mathcal I_i$ are
finite type quasi-coherent ideals on $X$, and take
$\pi\colon X'=\mathsf{CSepBl}_U(T_1,T_2)=\mathsf{SepBl}_U(Z_1,Z_2)\to X$.
By [lemma-nagata-constructible-closed-support],
$V(\mathcal J_i)=T_i$ in $U$. The restriction equality from
[lemma-nagata-extend-finite-type-ideal] consequently gives
$|Z_i\cap U|=T_i$, so $Z_1\cap Z_2\cap U=\varnothing$. By
[def-nagata-separate-closed-subschemes], $\pi$ is the blow-up of $X$ along
$\mathcal I_1+\mathcal I_2$ and is $U$-admissible, and by
[lemma-nagata-separate-closed-subschemes] the strict transforms of $Z_1$ and
$Z_2$ in $X'$ are disjoint. The closure of $\pi^{-1}(T_i)$ is contained in
the underlying set of the strict transform of $Z_i$: the strict transform is
closed in $X'$, and it contains every point lying both over the open
$X\setminus(Z_1\cap Z_2)$ preserved by the blow-up and over $Z_i$ — in
particular every point of $\pi^{-1}(T_i)$, since
$T_i\subseteq Z_i\cap U$ and $U\cap Z_1\cap Z_2=\varnothing$. The two strict
transforms are disjoint, so these two closures are disjoint as claimed.
