+++
id = "prose-08-01"
kind = "hidden"
title = "The six operations on $D^b_{\\mathrm{ctf}}$"
order = 373
+++
The previous sections give us $Rf_!$ and $f^!$, for every admissible
coefficient ring, on the categories $D^b_{\mathrm{ctf}}(-,\Lambda)$: proper direct
image preserves them (Proposition [sk-thm-sfb-proper-base-change]),
Brown representability provides the adjunction
(Theorem [sk-prop-sf-existence]), and the computation of $f^!$ through
the projective line and Deligne's theorem on $Rj_*$ shows that $f^!$
preserves them (Theorems [sk-prop-sf-rf-shriek-preservation]
and [sk-thm-restriction]). We first put these together into the proof of
Theorem [sk-thm-existence]. Two things are still missing before the
formalism can be used. The other four operations, $f^*$, $Rf_*$,
$\otimes^{\mathbf L}$ and $\cHom$, must also act on $D^b_{\mathrm{ctf}}$; Verdier duality,
for instance, is about $\cHom(-,a_X^!\Lambda)$, and the Künneth formulas
of the trace formula combine $Rf_*$ with tensor products. And we must be
able to move between coefficient rings, since the geometric arguments are
made with torsion coefficients and the eigenvalues of Frobenius live in
$\overline{\mathbf Q}_\ell$.

For torsion coefficients on the étale site, the finiteness theorems of
SGA 4 and SGA 4$\tfrac12$ [sga4, sga4-5] say that all six operations
preserve bounded constructible complexes of finite Tor amplitude. With
$\ell$-adic coefficients, Ekedahl [ekedahl90] obtained the same
statements by working with inverse systems $(K_n)$ and passing to a
quotient category, and each operation had to be defined on systems by
hand. On the pro-étale site the operations are the ordinary derived
functors of sheaves of modules, and the first result of the section is
that they restrict (Proposition [sk-thm-sf-ctf-stability]): $f^*$, $Rf_*$, $Rf_!$,
$f^!$, $\otimes^{\mathbf L}$ and $\cHom$ preserve $D^b_{\mathrm{ctf}}(-,\Lambda)$ for
every admissible $\Lambda$, and their adjunctions restrict there. The
direct images reduce, through a compactification, to proper direct images
and to $Rj_*$ for open immersions $j$, which we already control. For
$\cHom$ we use the formula

$$
\cHom(a_!P,K)\simeq Ra_*\bigl(P^\vee\otimes^{\mathbf L}a^!K\bigr)
$$

for a locally closed immersion $a$ and a locally constant perfect complex
$P$, so that internal Hom is expressed through $f^!$; this is one reason we
needed $f^!$ on $D^b_{\mathrm{ctf}}$ first. The functor $f^*$ is exact and is
handled sheaf by sheaf. For $\otimes^{\mathbf L}$ (and so for $\cHom$)
one cannot argue sheaf by sheaf, because a complex of finite Tor
amplitude may have cohomology sheaves of infinite Tor dimension: the
perfect complex $\mathbf Z/\ell^2\xrightarrow{\ell}\mathbf Z/\ell^2$ has
cohomology $\mathbf Z/\ell$ in two degrees. Instead we use that on the
strata of a finite stratification such a complex is locally
$\Lambda_S\otimes P$ with $P$ a perfect complex, and this description is
preserved by tensor product.

The second result concerns change of coefficients: from $\mathcal O_E$
to its finite quotients $A$, from $\mathcal O_E$ to $E$ and from $E$ to
$\overline{\mathbf Q}_\ell$, together with finite extensions of $E$ and maps between finite
rings. For
each operation there is a canonical comparison map, such as
$(Rf_*K)\otimes^{\mathbf L}\Lambda'\to Rf_*(K\otimes^{\mathbf L}\Lambda')$,
and these are isomorphisms on $D^b_{\mathrm{ctf}}$ (Proposition [sk-prop-scalar-six]).
The Tor condition is needed here. On a geometric point the
sheaf $\mathbf F_\ell$ lies in $\Dbc(\mathbf Z/\ell^2)$, but
$\mathbf F_\ell\otimes^{\mathbf L}_{\mathbf Z/\ell^2}\mathbf F_\ell$ has
$\mathbf F_\ell$ in every degree $\leq0$, so $\Dbc$ is not preserved by
reduction from $\mathbf Z/\ell^2$ to $\mathbf F_\ell$; this is why the
finite coefficient rings come with the category $D^b_{\mathrm{ctf}}$. For $f^!$ we
prove the comparison by computing $f^!$ once more, as for
constructibility, for a closed immersion and for $\mathbf P^1$, where it
comes down to the compatibility of the cycle class of the diagonal and
the trace with change of coefficients.

Together these results allow a statement that a canonical map is an
isomorphism to be proved with finite coefficients
(Proposition [sk-prop-reduction-to-finite]). For $\mathcal O_E$ both sides
are derived complete, so derived Nakayama reduces the claim to
$\mathcal O_E/\pi_E$; every object over $E$ is built from integral models
by cones and inverting $\ell$; and every object over $\overline{\mathbf Q}_\ell$ is defined
over a finite extension $E$ (Proposition [sk-prop-qlbar-two-colimit]). This is
how smooth base change (Theorem [sk-thm-sbc-coefficients]) and Verdier biduality
(Theorem [sk-thm-pd-verdier-duality]) pass from torsion to $\ell$-adic
coefficients. The principle applies to isomorphisms between
functors built from the six operations, not to the construction of maps:
the cycle class of the diagonal and the adjunction
$Rf_!\dashv f^*(d)[2d]$ for smooth $f$ must be built as single morphisms
with $\mathcal O_E$-coefficients.

From now on we work in $D^b_{\mathrm{ctf}}$ without further
comment and pass between $\mathcal O_E$, $E$, $\overline{\mathbf Q}_\ell$ and finite rings
whenever a statement is easier for one of them, as in the trace formula and
in the proof of the Weil conjectures.
