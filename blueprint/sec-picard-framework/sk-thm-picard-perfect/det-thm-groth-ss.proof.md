+++
kind  = "proof"
of    = "det-thm-groth-ss"
+++
*Step 1 (the double complex).* A Grothendieck abelian category has
enough injectives, so $A$ has an injective resolution $A\to I^\bullet$
in $\mathcal A$. Put $C^\bullet=\Phi(I^\bullet)$, a complex in
$\mathcal B$ concentrated in degrees $\ge0$ with
$\mathcal H^q(C^\bullet)=R^q\Phi(A)$. As $\mathcal B$ has enough
injectives, $C^\bullet$ has a Cartan–Eilenberg resolution
$C^\bullet\to J^{\bullet,\bullet}$; set $D^{p,q}=\Psi(J^{p,q})$, a
first-quadrant double complex in $\mathcal C$.

*Step 2 (filtration by the second degree).* For fixed $p$ the column
$J^{p,\bullet}$ is an injective resolution of $C^p=\Phi(I^p)$, so the
first spectral sequence of $D$ has
$E_1^{p,q}=R^q\Psi\bigl(\Phi(I^p)\bigr)$, which vanishes for $q>0$
because $\Phi(I^p)$ is $\Psi$-acyclic (the acyclicity hypothesis). The
sequence therefore collapses on the bottom edge, and as $I^\bullet$ is an
injective resolution of $A$,

$$
H^n(\operatorname{Tot}D)\cong
\mathcal H^n\bigl(\Psi\Phi(I^\bullet)\bigr)=R^n(\Psi\circ\Phi)(A) .
$$

*Step 3 (filtration by the first degree).* By the defining property
of a Cartan–Eilenberg resolution, the horizontal cohomology objects of
$J^{\bullet,\bullet}$ form injective resolutions of the
$\mathcal H^q(C^\bullet)$, split compatibly with the cycles and
boundaries; hence the other spectral sequence of the same double complex
has

$$
E_2^{p,q}=R^p\Psi\bigl(\mathcal H^q(C^\bullet)\bigr)=R^p\Psi\bigl(R^q\Phi(A)\bigr).
$$

Both spectral sequences abut to $H^\bullet(\operatorname{Tot}D)$, which
Step 2 identifies with $R^{p+q}(\Psi\circ\Phi)(A)$; this is the displayed
first-quadrant spectral sequence, with the image filtration of
[det-def-groth-ss] on the abutment, finite in each degree.

*Step 4 (morphisms of sites).* The categories of abelian sheaves on
the sites $X$, $Y$, $Z$ are Grothendieck abelian, and $f_*$, $h_*$ are
additive and left exact. The functor $f^{-1}$ is exact and left adjoint
to $f_*$, so $f_*$ carries injectives to injectives, and an injective
sheaf is $h_*$-acyclic. Hence $(\Phi,\Psi)=(f_*,h_*)$ is a composable
pair with acyclicity in the sense of [det-def-groth-ss], and since
$(hf)_*=h_*f_*$ the theorem gives the spectral sequence
$R^ph_*R^qf_*F\Rightarrow R^{p+q}(hf)_*F$. For $Z$ the punctual site,
$h_*=\Gamma(Y,-)$ and $(hf)_*=\Gamma(X,-)$, which is the Leray spectral
sequence; the Zariski sites of schemes are a special case.

*Step 5 (the Zariski coherent case).* On $\cO$-modules (again a
Grothendieck abelian category) the composite is
$\Gamma(Y,-)\circ f_*=\Gamma(X,-)$, but $f^*$ is no longer exact, so
acyclicity is supplied differently: an injective $\cO_X$-module $\cI$ is
flasque (apply injectivity to $j_!\cI|_U\to\cI$ for
$j:U\hookrightarrow X$ open to extend a section over $U$), $f_*$
preserves flasqueness, and a flasque module is $\Gamma$-acyclic on every
open. So $(f_*,\Gamma(Y,-))$ is again a composable pair with acyclicity
in the sense of [det-def-groth-ss], and the theorem applies; for proper
$f$ and coherent $F$ this is the Zariski sequence of the statement.

The topos form of the sequence and of the acyclicity criterion are
Stacks, Cohomology on Sites, Lemmas 21.14.5/21.14.6
([`0732`](https://stacks.math.columbia.edu/tag/0732),
[`0733`](https://stacks.math.columbia.edu/tag/0733)), and
for ringed spaces Lemmas 20.13.4/20.13.8
([`01F2`](https://stacks.math.columbia.edu/tag/01F2),
[`01F6`](https://stacks.math.columbia.edu/tag/01F6)).
