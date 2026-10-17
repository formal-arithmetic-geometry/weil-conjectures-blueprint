+++
kind = "proof"
of = "sk-cor-trace"
uses = ["sk-thm-sf-identification", "sk-prop-scalar-six", "sk-def-ops", "sk-thm-regular", "sk-thm-smooth-purity", "sk-thm-purity-transport", "sk-thm-derived-duality", "sk-def-trace-cup"]
+++
With finite coefficients, étale cohomology of a $d$-dimensional scheme over an
algebraically closed field vanishes above degree $2d$; this bound was used for
the finite-Tor direct-image estimates. Connectedness gives $H^0=\Lambda$. First
take $\Lambda=\mathbf Z/\ell^n$. This ring is self-injective, so
$R\operatorname{Hom}_{\mathbf Z/\ell^n}(-,\mathbf Z/\ell^n)$ has cohomology equal
to the ordinary dual of the opposite cohomology. Derived Poincaré duality in
degree zero then identifies $H^{2d}(X,\mathbf Z/\ell^n(d))$ with
$\Hom(H^0(X,\mathbf Z/\ell^n),\mathbf Z/\ell^n)=\mathbf Z/\ell^n$, and the map is
the smooth trace by the identification of the pairing in
Theorem [sk-thm-sf-identification].

Every finite $A$ is an algebra over some $\mathbf Z/\ell^n$. By
Proposition [sk-prop-scalar-six], the constant-coefficient complexes and their
traces over $A$ are obtained by derived extension of scalars from
$\mathbf Z/\ell^n$. For a complex with cohomology in degrees $\le2d$, derived
extension of scalars identifies the degree $2d$ cohomology with the ordinary
tensor product of the degree $2d$ cohomology. Therefore the top cohomology is
$A$, the trace is an isomorphism, and the same upper bound holds.

At $\mathcal O_E$, use the normalized finite reductions and their derived
inverse-limit reconstruction. The finite cohomology groups at each level satisfy
the Mittag–Leffler condition, since they are finite; hence there is no
$\lim^1$ contribution to the top group. The compatible top traces give
$H^{2d}(X,\mathcal O_E(d))=\mathcal O_E$, with the same vanishing bounds.
Localization and filtered finite-extension scalar change give
$\Ql,E,\overline{\mathbf Q}_\ell$. The lower bound and $H^0$ also follow directly
from ordinary sheaf cohomology and connectedness.

For the point class, the composite of the closed-support counit with the smooth
trace is, by composition of exceptional adjunctions, the counit of
$a_Xx=\mathrm{id}$. It takes $1$ to $1$. This proves normalization for the class
defined in the statement directly from the counits. In smooth local coordinates
it agrees with the successive Kummer parameter class, by the normalization of
the smooth orientation.

*Complement.*

*(i)* Let $c:\Lambda\to R\Gamma(X,\Lambda_X(d))[2d]$ be a class in
$H^{2d}(X,\Lambda_X(d))$, and let $c^\flat:\Lambda_X=a_X^*\Lambda\to
\Lambda_X(d)[2d]\simeq\omega_X$ be its adjoint for $a_X^*\dashv Ra_{X*}$, and
$c^\sharp=\epsilon_{a_X}\circ Ra_{X!}(c^\flat):Ra_{X!}\Lambda_X\to\Lambda$ the
adjoint of $c^\flat$ for $Ra_{X!}\dashv a_X^!$; here $Ra_{X!}\simeq Ra_{X*}$
because $X$ is proper ([sk-def-ops]). The class $1\in H^0(X,\Lambda_X)$ is the
unit $\eta:\Lambda\to Ra_{X*}a_X^*\Lambda=R\Gamma(X,\Lambda_X)$. Since
$c=Ra_{X*}(c^\flat)\circ\eta$,

$$
c^\sharp\circ\eta=\epsilon_{a_X}\circ Ra_{X*}(c^\flat)\circ\eta
=\epsilon_{a_X}\circ c ,
$$

and the right side is $\operatorname{tr}_X(d)(c)$: the counit $\epsilon_{a_X}$ read
through $\Lambda_X(d)[2d]\simeq\omega_X$. The map $c\mapsto c^\sharp$ is the
degree-zero part of the duality of [sk-thm-sf-identification] for
$K=\Lambda_X$, whose adjoint pairing is formed from evaluation and the same
counit.

*(ii)* Let $\Lambda=A_{E,n}$. Since $X$ is smooth over the algebraically closed
field $k$, the point $x:\operatorname{Spec}k\hookrightarrow X$ is a regular closed
immersion of codimension $d$ with $a_X\circ x=\mathrm{id}_{\operatorname{Spec}k}$,
and $\operatorname{Spec}k$ is regular, so [sk-thm-regular] applies with $c=d$. By
[sk-thm-regular](c), $[x\subset X]=\operatorname{cl}_x(1)$ is the image of $1$
under the isomorphism $\Lambda\simeq x^!\Lambda_X(d)[2d]$ assembled from the
orientations of $a_X$ and of $a_{\operatorname{Spec}k}=\mathrm{id}$ through the
composition law $x^!a_X^!\Lambda\simeq(a_Xx)^!\Lambda=\Lambda$; the orientation of
the identity is the identity of $\Lambda$, by the compatibility with composition
in [sk-thm-smooth-purity] applied to $\mathrm{id}=\mathrm{id}\circ\mathrm{id}$.
Read through $\omega_X\simeq\Lambda_X(d)[2d]$, this is the isomorphism
$x^!\omega_X\simeq\Lambda$ of the statement. Forgetting supports is
$R\Gamma(X,-)$ applied to the counit $x_*x^!\to\mathrm{id}$, so $[x]$ is the image
of $[x\subset X]$. Étale locally at $x$, $[x\subset X]$ is the frame class
$\partial\kappa(t_1)\cup\dots\cup\partial\kappa(t_d)$ of [sk-thm-regular](b);
this is the sense in which the trace is normalized by the fundamental class of
[sk-prop-an].

The frame classes of [sk-thm-regular] are built from Kummer classes, boundaries
and cup products, which reduce to their counterparts under
$A_{E,n}\to A_{E,m}$; so $([x\subset X]_n)_n$ is a compatible system, which
defines $[x\subset X]$ over $\Oe$, and its images define it over $E$ and $\Qlb$.
At these stages $\operatorname{tr}_X$ is the transported counit read through the
transported orientation, compatibly with the finite reductions and with scalar
extension ([sk-thm-purity-transport]). Hence the identification of $[x]$ with the
image of $[x\subset X]$ holds at every stage.

*(iii)* Take $K=\Lambda_X$, so $K^\vee=\Lambda_X$, in Corollary
[sk-thm-derived-duality] for proper $X$: the pairings
$H^i(X,\Lambda)\times H^{2d-i}(X,\Lambda(d))\to\Lambda$ are perfect. By
[sk-thm-sf-identification] they are cup product followed by
$\operatorname{Tr}_X$; removing the twist gives the displayed pairings with values
in $\Lambda(-d)$, which are the trace–cup pairings of [sk-def-trace-cup].
Graded commutativity of the cup product gives
$x\cup y=(-1)^{i(2d-i)}y\cup x$ for $x\in H^i$, $y\in H^{2d-i}$, and
$i(2d-i)\equiv i\pmod 2$. For $i=d$ the sign is $(-1)^d$; if $d$ is odd and
$2$ is invertible in $\Lambda$, then $\langle x,x\rangle=-\langle x,x\rangle$
forces $\langle x,x\rangle=0$.
