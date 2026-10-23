+++
kind  = "proof"
of    = "sk-lem-walg-engel"
+++
We prove that the common kernel is nonzero by induction on
$\dim\mathfrak n$, the case $\dim\mathfrak n=0$ being clear. Choose a
maximal proper subalgebra $\mathfrak a\subsetneq\mathfrak n$. If $X^r=0$,
then

$$
(\operatorname{ad}X)^m(Y)=\sum_{i=0}^m(-1)^i\binom mi X^{m-i}YX^i,
$$

so that $(\operatorname{ad}X)^{2r-1}=0$. Hence the image of $\mathfrak a$
in $\operatorname{End}(\mathfrak n/\mathfrak a)$ consists of nilpotent
endomorphisms, and the induction hypothesis gives an element
$Y\notin\mathfrak a$ with $[\mathfrak a,Y]\subseteq\mathfrak a$. Thus the
normalizer of $\mathfrak a$ strictly contains $\mathfrak a$. By
maximality, this normalizer is all of $\mathfrak n$, that is,
$\mathfrak a$ is an ideal. The quotient $\mathfrak n/\mathfrak a$ has
dimension one, since otherwise the inverse image of a one-dimensional
subalgebra of the quotient would be an intermediate proper subalgebra.

By induction, the common kernel $M^{\mathfrak a}$ is nonzero, and it is
$\mathfrak n$-stable because $\mathfrak a$ is an ideal. Choose $X$ mapping
to a basis of $\mathfrak n/\mathfrak a$. The restriction of $X$ to
$M^{\mathfrak a}$ is nilpotent and therefore has a nonzero kernel, which
consists of vectors killed by all of $\mathfrak n$. Applying this
assertion to the quotient of $M$ by such an invariant line and arguing by
induction on $\dim M$, we obtain a basis in which every element of
$\mathfrak n$ is strictly upper triangular. Sufficiently long iterated
brackets of such matrices vanish.
