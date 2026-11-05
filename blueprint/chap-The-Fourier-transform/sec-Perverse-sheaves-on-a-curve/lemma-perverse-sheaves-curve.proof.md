+++
kind = "proof"
of = "lemma-perverse-sheaves-curve"
order = 1250
uses = ["lemma-largest-punctual-subsheaf"]
+++
The truncation triangle of $K$ splits $\mathcal H^0K$ into its largest
punctual subsheaf, which goes into ${}^pD^{\le0}$, and the quotient,
which goes into ${}^pD^{\ge1}$, using
Lemma [lemma-largest-punctual-subsheaf].

The shift axioms are immediate from the definitions. For orthogonality, if
$A\in{}^pD^{\le0}$ and $B\in{}^pD^{\ge1}$, then ordinary truncation
identifies $\Hom(A,B)$ with
$\Hom(\mathcal H^0A,\mathcal H^0B)$, which is zero because the source
is punctual and the target has no punctual subsheaf.
To construct the truncation triangle for $K$, put $K'=\tau^{\le0}K$
and $F=\mathcal H^0K$, and let $A$ be the fibre of
$K'\to F/F_{\rm p}$. Then the cohomology of $A$ is that of $K$ below zero,
and $\mathcal H^0A=F_{\rm p}$, so that $A\in{}^pD^{\le0}$.
By the octahedral axiom, applied to $A\to K'\to K$, we obtain a
triangle $A\to K\to B\to$, in which the cone $B$ is an extension of
$\tau^{\ge1}K$ by $F/F_{\rm p}$ in degree zero, so it
has no negative ordinary cohomology and
$\mathcal H^0B=F/F_{\rm p}$. Since $F/F_{\rm p}$ has no punctual
subsheaf by Lemma [lemma-largest-punctual-subsheaf],
$B\in{}^pD^{\ge1}$. Finally, the t-structure is bounded because the ordinary
one is.

The heart of any t-structure is abelian, with kernels
and cokernels computed from the perverse cohomology of a cone
[bbd82, Théorème 1.3.6]; the proof uses only the octahedral axiom and
orthogonality. Punctual sheaves in degree zero clearly lie in the
heart. So does $(j_*M)[1]$, since $j_*M$ has no punctual subsheaf, as
follows from Lemma [lemma-largest-punctual-subsheaf] applied
to $F=j_*M$, for which $F_{\rm p}=0$.
