+++
id = "prose-07-01"
kind = "hidden"
title = "The six operations on $\\Dctf$"
order = 622
+++
Smooth base change and Verdier biduality will be proved with torsion
coefficients, as were proper base change and Deligne's theorem on $Rj_*$.
The Weil conjectures, however, need them over $\overline{\mathbf Q}_\ell$, where Frobenius
eigenvalues live. This section provides the principle that carries every
such statement across. A canonical map built from the six operations is an
isomorphism for all admissible $\Lambda$ as soon as it is one for every
finite ring (Proposition [proposition-isomorphisms-reduce-finite-coefficients]).

For $\mathcal O_E$ both sides are derived complete, and by derived Nakayama
it suffices to check the map modulo $\pi_E$. For instance, let $K$ be in
$D^b_{\mathrm{ctf}}(X,\mathcal O_E)$. Both sides of the biduality map
$K\to\mathbb D_X\mathbb D_XK$ are derived complete. Modulo $\pi_E$, moreover, the map is biduality with $\mathbf F_E$-coefficients, which is an isomorphism.
Hence the biduality map is an isomorphism. From there we pass to $E$ and $\overline{\mathbf Q}_\ell$: every object over $E$ is built by cones from integral models with $\ell$ inverted, and every object over $\overline{\mathbf Q}_\ell$ is defined over a finite extension $E$
(Proposition [proposition-dctf-x-qbar-2-colimit]). In this way smooth base
change (Theorem [theorem-smooth-base-change-all-admissible]) and Verdier
biduality (Theorem [theorem-verdier-biduality]) pass from torsion to
$\ell$-adic coefficients.

The principle needs two things, and neither is formal. First, both sides
must lie in $D^b_{\mathrm{ctf}}(-,\Lambda)$. Thus all six operations must preserve these
categories, and not only $Rf_!$ and $f^!$, which we now control
(Theorem [theorem-exceptional-inverse-image],
Section [sec-Proof-of-the-theorem]). Second, each operation must commute with
change of coefficients. For $f^*$ and $\otimes^{\mathbf L}$ this is clear, since a change of coefficients is itself a tensor product. For a right adjoint, however, it is a real statement. For example, consider a map of finite rings $A\to B$; then the isomorphism $R\Gamma(X,K)\otimes^{\mathbf L}_AB\simeq
R\Gamma(X,K\otimes^{\mathbf L}_AB)$ is a projection formula, and it uses
finite cohomological dimension. Next consider $\mathcal O_E\to E$. Since
$E$ is the colimit of the modules $\pi_E^{-n}\mathcal O_E$, the comparison
says that $Rf_*$ commutes with a filtered colimit. This holds because the
terms are uniformly bounded below.

Internal Hom causes a further difficulty, because it hides the exceptional
inverse image. For a closed immersion $i$ we have

$$
\cHom(i_*\Lambda,K)\simeq i_*i^!K .
$$

Before we can say anything about $\cHom(K,L)\otimes^{\mathbf L}\Lambda'$, we
must therefore know how $i^!$ behaves under change of coefficients. The comparison map for $f^!$ is defined by adjunction, and to show that it is an isomorphism we compute $f^!$ once more, for a closed immersion and for
$\mathbf P^1$. For $\mathbf P^1$, for instance, it comes down to the compatibility of the
cycle class of the diagonal and of the trace with change of coefficients
(Proposition [proposition-six-operations-change-coefficients]).

The first requirement needs no construction: on the pro-étale site the
six operations are the ordinary derived functors of sheaves of modules, and
we only check that they preserve $D^b_{\mathrm{ctf}}(-,\Lambda)$
(Proposition [proposition-six-operations-dctf]).
For torsion coefficients on the étale site, these finiteness theorems are in SGA 4 and
SGA 4$\tfrac12$ [sga4], [sga4-5]. In general, the work is in $Rf_*$ and in $\cHom$ (Section [sec-Stability-of-Dbctf]). There, a compactification reduces $Rf_*$ to proper direct image and $Rj_*$, while the formula above and its
analogue for open immersions express $\cHom$ through $Ra_*$, $a^!$ and
tensor products. Tensor products, finally, are handled by the local description of a
complex of finite Tor amplitude: on the strata of a finite stratification
it is locally $\Lambda_S\otimes P$ with $P$ perfect
(Section [sec-Finite-Tor-amplitude]).

From now on we work in $D^b_{\mathrm{ctf}}$ without further comment and pass between
$\mathcal O_E$, $E$, $\overline{\mathbf Q}_\ell$ and finite rings whenever a statement is easier for
one of them, as in the trace formula and in the proof of the Weil conjectures.
