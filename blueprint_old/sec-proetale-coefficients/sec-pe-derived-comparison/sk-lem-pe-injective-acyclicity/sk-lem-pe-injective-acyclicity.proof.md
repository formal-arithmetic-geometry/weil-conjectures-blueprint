+++
kind = "proof"
of = "sk-lem-pe-injective-acyclicity"
uses = ["det-pe-injective-acyclicity-reduction", "lem-weil-pbc-comparison-injective-acyclicity", "lem-weil-pbc-cech-criterion", "lem-weil-pbc-proetale-restriction-injectives", "sk-thm-pe-indetale-refinement", "sk-prop-pe-comparison-morphism"]
+++
A pro-étale cover of an affine is a limit of étale
covers, so its Čech complex for $\nu_X^*I$ is a filtered
colimit of étale Čech complexes for $I$, which are acyclic.
The sheaf $R^q\nu_{X,*}\nu_X^*I$ is associated to
$V\mapsto H^q(V_{\mathrm{pro}\acute{e}t},\nu_X^*I)$, so it suffices to show that
positive cohomology vanishes on affine étale objects $V$. The
restriction of $I$ to $V_{\acute{e}t}$ is injective, since restriction has an
exact left adjoint, namely extension by zero. Hence we may assume $X$ affine.
By Theorem [sk-thm-pe-indetale-refinement], every pro-étale covering of
an affine object is refined by a finite covering by affines that are
ind-étale over it. By the Čech acyclicity criterion for a basis,
it therefore suffices to show that the Čech complexes of $\nu_X^*I$
for such coverings have no positive cohomology.

We claim that the Čech complex of such a covering is a
filtered colimit of Čech complexes of étale coverings. Write each
covering map as an inverse limit of affine étale maps
over the object being covered. By (2.6), the
Čech complex of the covering is the filtered colimit of the
Čech complexes of these étale approximations. Each finitely
presented approximation descends to a common étale stage over the
base, becomes a covering after increasing that stage, and its nerve
descends by taking fibre products. Each augmented Čech complex at
a finite stage is obtained by applying $\Hom(-,I)$ to the exact augmented
complex of free sheaves of $\Lambda$-modules on the nerve, so it has no
positive cohomology because $I$ is injective. Filtered colimits are exact, so the same holds for the
pro-étale covering, and the criterion implies the required vanishing.
This is the argument of [Stacks, Tag 099U](https://stacks.math.columbia.edu/tag/099U).
