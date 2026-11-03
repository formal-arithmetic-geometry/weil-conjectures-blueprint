+++
kind  = "proof"
of    = "lem-chow-graph"
uses = ["def-nagata-dense-compactification", "def-nagata-scheme-image-comparison", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "lem-chow-segre", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-universal", "lemma-nagata-scheme-theoretic-closure-minimal"]
+++
*Part (1).* By definition the scheme-theoretic image $Z$ is a closed
subscheme of $P:=\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S$
([def-nagata-scheme-theoretic-image]), so $Z\to P$ is a closed immersion.
$P\to S$ is proper, being a finite fibre product of proper $S$-schemes, and
$Z$ is a closed subscheme of it, so $Z\to S$ is proper by 01W5. The Segre
embedding $P\hookrightarrow\mathbf P^N_S$, $N$ a finite set, is a closed
immersion of $S$-schemes ([lem-chow-segre]); composing it with $Z\to P$
gives the closed immersion $Z\to\mathbf P^N_S$ of $S$-schemes.

*Part (2).* Each $j_i|_U$ is an immersion, being the composition of the open immersion
$U\to U_i$ with the immersion $j_i$. Hence $j$ is an immersion by
[lem-chow-tuple-immersion], and it is quasi-compact because $U$ is
noetherian. Part (2) now follows from 01RG applied to the quasi-compact
immersion $j$.

*Part (3).* The open immersion $U\to Z$ is quasi-compact and scheme-theoretically
dominant, so $\mathrm{pr}_i|_Z\colon Z\to\mathbf P^{n_i}_S$ and its restriction
$\mathrm{pr}_i\circ j=j_i|_U$ to $U$ have the same kernel. That kernel
contains the ideal sheaf of $Z_i$, because $j_i|_U$ factors through $Z_i$ by
construction; so the universal property of the closed immersion
$Z_i\to\mathbf P^{n_i}_S$ produces the morphism $p_i\colon Z\to Z_i$ with
$p_i$ followed by $Z_i\to\mathbf P^{n_i}_S$ equal to $\mathrm{pr}_i|_Z$. (This
is 01R9 in the case in which $Z_i$ is presented as the
scheme-theoretic image of $j_i|_U$, which it is: formation of the
scheme-theoretic image commutes with restriction to the open $U_i\subseteq X$.)
It is proper: $Z\to S$ is proper by (1) and $Z_i\to S$ is separated, so $p_i$
is proper by 01W6.

*Part (4)* is immediate from $\mathrm{pr}_i\circ j=j_i|_U$ and the fact that
$j_i$ identifies $U_i$ with an open subscheme of $Z_i$.
