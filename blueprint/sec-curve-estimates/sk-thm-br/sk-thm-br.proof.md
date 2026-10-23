+++
kind = "proof"
of = "sk-thm-br"
+++
We compute on $C_{\mathrm{ét}}$. Descent for invertible modules identifies
$\mathbf G_m$-torsors with line bundles ([thm-sc-hilbert-90]), which gives
the assertion in degree one. In degrees at least two we use the theorem that
$H^q(C_{\mathrm{ét}},\mathbf G_m)=0$ for $q\geq2$ on a smooth curve over an
algebraically closed field (Stacks, Tag 03RM). Its proof combines the divisor
sequence of rational functions and their discrete valuations
([lem-sc-divisor-sequence-general]) with the Galois cohomology of the function field
$K=k(C)$; the geometric input is Tsen's theorem ([lem-sc-tsen]), which we
recall.

Tsen's theorem says that $K$ is $C_1$ ([def-sc-cr-field]): a homogeneous form of
degree $d$ in $m>d$ variables has a nonzero zero. On a smooth proper model,
bound the poles of its coefficients by a divisor $D$ and let the unknowns
range over $H^0(C,\cO_C(NH))$ for an ample divisor $H$. The value of the form
then lies in $H^0(C,\cO_C(dNH+D))$. By Riemann–Roch there are
$mN\deg H+O(1)$ unknown coefficients and $dN\deg H+O(1)$ homogeneous
equations. For large $N$ the first number is larger, so over the
algebraically closed field $k$ the equations have a nonzero solution
(Stacks, Tag 03RD).

The reduced norm form of a division algebra of degree $d>1$ over $K$ has
degree $d$ in $d^2>d$ variables and does not vanish on a nonzero element.
Tsen's theorem therefore gives $\operatorname{Br}(K)=0$ (Stacks, Tag 03RF).
The same holds for every finite extension of $K$, since it is again the
function field of a curve over $k$. The vanishing of the Brauer group is one ingredient; (Stacks, Tag 03RM)
combines it with the discrete-valuation calculation and the cohomology of
the function field to obtain vanishing in every degree $q\geq2$ (for $q=2$
this is also the route $\Br(C)\hookrightarrow\Br(k(C))=0$ of
[lem-sc-brauer-injectivity]).

Finally [sk-prop-sf-comparison] transports these identifications to
$C_{\mathrm{proét}}$. The comparison maps, the torsor identifications and the
restriction maps are functorial, which gives the stated naturality.
