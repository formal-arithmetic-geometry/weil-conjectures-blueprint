+++
id = "prose-07-11"
kind = "hidden"
title = "Generic constructibility of direct image along an open immersion"
order = 345
+++
We can now assemble Deligne's generic base change theorem, in the form we
need; over a field it gives the finiteness of $Rj_*$
(Corollary [sk-cor-geo-open-finiteness]), which is all that the
computation of $f^!$ requires. Base change can only hold over a dense
open of $S$: for the punctured plane over the $t$-line, $R^1j_*\Lambda$
vanishes on $\mathbf A^2$ but not on the fibre over $t=0$.

The proof is an induction on the dimension $n$ of the generic fibre, in
three steps. Step 1 uses the coordinate projections and the induction
hypothesis over $\mathbf A^1_S$ to obtain the theorem away from a closed
subset finite over $S$. Step 2 treats a smooth $X$ and a locally constant
$F$, as explained before Lemma [sk-lem-geo-finite-boundary]. Step 3 reduces the
general case to Step 2 by shrinking $X$ to a dense open $V$ on which $F$
is locally constant and $X$ is smooth over $S$; the error term lives on
$X\setminus V$, whose generic fibre has dimension less than $n$. In
characteristic $p$ the generic fibre need not contain a smooth dense open:
for $X=\mathbf A^1_{\mathbf F_p}$ mapping to the $t$-line by $x\mapsto x^p$,
the generic fibre is $\operatorname{Spec}\mathbf F_p(t^{1/p})$, which is not
smooth over $\mathbf F_p(t)$. This is why a finite universal
homeomorphism of the base is allowed in Step 3. It changes neither the
étale topoi nor the conclusion.
