+++
id = "prose-12-14"
kind = "hidden"
title = "Additivity of trace classes"
order = 564
+++
The Lefschetz–Verdier formula expresses the trace as a sum of local
terms but does not compute them. To compute local terms, we cut $K$
into pieces along decompositions of $X$ into an open and a closed part
which are invariant under the correspondence, and for this we need the
trace class to be additive. For the trace of an endomorphism of a
perfect complex, additivity says that a block triangular matrix has
trace equal to the sum of the traces of its diagonal blocks, and by
Remark [sk-rem-tf-coherent-additivity] it can only be expected for
filtrations lifted to the filtered derived category. The trace class
needs the same care. We lift each step of the construction of the trace
morphism to filtered complexes. The components of $u$ that a filtered
lift allows besides the diagonal ones, maps from $K_a$ to $K_{a+r}$ with
$r>0$, do not contribute: $\omega_X$ carries the trivial filtration, in
filtration degree $0$, so the part of evaluation in graded degree zero
sees only the diagonal components $K_a\to K_a$.

For an open $U$ with closed complement $Z$, the correspondence must
respect the decomposition, and the condition is
$c_1^{-1}(Z)\subset c_2^{-1}(Z)$. For the graph of an endomorphism
$\varphi$, where $c_1=\operatorname{id}_X$ and $c_2=\varphi$, it says
that $\varphi(Z)\subset Z$. Under this condition there are no nonzero
maps from $Rc_{1!}c_2^*K_U$ to $K_Z$, so $u$ restricts to $K_U$ in an
essentially unique way, and the filtered lift is unique up to
contractible choice.
We apply the result in Proposition [sk-p-frob], with
$Z$ a single fixed point of Frobenius.
