+++
id = "prose-09-05"
kind = "hidden"
title = "Statement (4)"
order = 732
+++
We recall what $D^b_{\mathrm{ctf}}$ means for each coefficient ring. For integral
coefficients and for coefficients in a field, $D^b_{\mathrm{ctf}}=\Dbc$, and we write
$\Dbc$ in calculations that only concern these cases. With integral
coefficients finite Tor amplitude is automatic, and membership in
$\Dbc(T,\mathcal O_E)$ can be tested modulo $\ell$
(Proposition [proposition-integral-constructibility-criterion]).

The proof passes through finite rings $A$ with $\ell^rA=0$, such as
$\mathcal O_E/\ell^n$. For these, $D^b_{\mathrm{ctf}}$ is the category of
Definition [definition-constructible-sheaves], which on the pro-étale
site is identified with the pullback of its étale counterpart
(Corollary [corollary-finite-tor-amplitude-under-comparison]). Here the Tor
condition makes derived change of coefficients preserve boundedness, as the
example after
Proposition [proposition-six-operations-change-coefficients] shows. When we
compare coefficient rings, we write the ring as a subscript of the functor, as
in $Rf_{!,A}$ or $f^!_{\mathcal O_E}$; otherwise we omit the subscript.

With coefficients $A$, we have $Rf_!=R\bar f_*\circ j_!$ for a
compactification $f=\bar f\circ j$, and on $D^b_{\mathrm{ctf}}$ these functors and their
right adjoints are those of
Theorem [theorem-existence-exceptional-inverse-image], restricted in
Theorem [theorem-f-shriek-finite-coefficients]. Proper base change, the
projection formula and the localization triangle are the identities of
Section [sec-Conventions-2], which we may prove on the étale
sites by Proposition [proposition-comparison-etale-derived-category]. For an
étale map, extension by zero is exact on sheaves of $A$-modules on the
pro-étale sites; on the derived categories it is left adjoint to inverse
image, and the counit is given on geometric stalks by the sum over the
fibre.

Property (2) implies that the exceptional base change map is an
isomorphism for smooth $f$, because $\gamma_f$ and $\gamma_{f'}$ are
isomorphisms.

For étale $f$ we have $d=0$, and the theorem says that
$f^{!}\simeq f^{*}$ for every admissible $\Lambda$. For a smooth curve $C$
with structure map $a:C\to\operatorname{Spec}k$, it gives
$a^!\mathbf Z_{\ell,\operatorname{Spec}k}\simeq\mathbf Z_{\ell,C}(1)[2]$,
a single sheaf in degree $-2$.

For smooth $f$ the whole functor $f^!$ is determined by its value on
the constant sheaf, through the map
$f^*K\otimes^{\mathbf L}f^!\Lambda_Y\to f^!K$ of
Proposition [proposition-exceptional-inverse-image-smooth-morphism](2).
Smoothness is needed here, as the following example shows. Let $i:y\to C$
be the inclusion of a rational point of a smooth curve, with open
complement $j:U\to C$, and take $K=j_!\Lambda_U$. Then the analogous map
$i^*K\otimes^{\mathbf L}i^!\Lambda_C\to i^!K$ has source zero, since the
stalk of $j_!\Lambda_U$ at $y$ vanishes, but the localization triangle gives
$i^!j_!\Lambda_U\simeq(i^*Rj_*\Lambda_U)[-1]\neq0$.

We give $f^!\Lambda_Y$ a name rather than working with $\Lambda_X(d)[2d]$
directly, because the two are not yet known to be isomorphic. Moreover, the
complex $f^!\Lambda_Y$ is attached to $f$ without choices, and it satisfies base change
(Proposition [proposition-exceptional-inverse-image-smooth-morphism](3)).
Proving the theorem thus amounts to constructing an isomorphism between it and
$\Lambda_X(d)[2d]$ that does not depend on charts. In this sense the complex
is the analogue of the shifted orientation sheaf $\mathrm{or}_{X/Y}[m]$, and
for the structure map of a smooth scheme it is the dualizing complex of Poincaré
duality (Corollary [corollary-dualizing-complex-smooth-scheme]
and Theorem [theorem-poincare-duality]).
