+++
kind  = "proof"
of    = "lemma-nagata-two-open-density-transport"
uses = ["def-nagata-two-open-boundary-loci", "lemma-nagata-boundary-loci"]
+++
The initial copies of $U$ are scheme-theoretically dense by hypothesis.
Every graph, boundary-separation, and final modification in the displayed
diagram is $U$-admissible, so
[lemma-nagata-admissible-blowup-preserves-density] identifies the
inverse image of $U$ at each stage as a scheme-theoretically dense open.
The compatibility of the chosen copies of $U$ through a finite composite is
the conclusion of
[lemma-nagata-admissible-blowup-comp]. Therefore the common copy of
$U$ is dense in each of the final chart opens $W'_1$ and $W'_2$.

Let $F\subseteq W$ be closed and contain the image of
$U_1\cap U_2$. Its inverse image in each open chart $W'_i$ is closed and
contains the dense image of $U_1\cap U_2$, hence equals $W'_i$. Since the
two charts cover $W$ by
[lemma-nagata-two-open-final-modification], $F=W$, proving density.
The source $U_1\cap U_2$ is quasi-compact because $S$ is Noetherian,
$U\to S$ is of finite type, and every open subscheme of the resulting
Noetherian scheme $U$ is quasi-compact. Each map to $W'_i$ is a composite
of a quasi-compact open
immersion with finitely many blow-ups, which are quasi-compact; the finite
open cover then proves that $U_1\cap U_2\to W$ is quasi-compact.
