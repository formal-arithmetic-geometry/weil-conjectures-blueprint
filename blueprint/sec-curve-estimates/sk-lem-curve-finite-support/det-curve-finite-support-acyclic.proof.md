+++
kind = "proof"
of = "det-curve-finite-support-acyclic"
+++
*Part 1.* The closed immersion $i$ is finite, so by the finite stalk formula
([lemma-weil-pbc-finite-stalk-formula]) the stalk of $i_*i^{-1}F$ at a
geometric point $\bar x$ is $F_{\bar x}$ if $\bar x$ lies over $Z$ and $0$
otherwise, and the unit induces the identity on the stalks over $Z$. By the
support hypothesis the unit is an isomorphism on all geometric stalks, hence
an isomorphism ([lemma-weil-pbc-geometric-stalk-conservative]).

*Part 2.* The direct image $i_*$ is exact
([lemma-weil-pbc-finite-direct-image-exact]) and has the exact left adjoint
$i^{-1}$, so it preserves injectives and
$H^q(C,i_*G)=H^q(Z,G)$ for every sheaf $G$ on $Z$. The scheme $Z$ is
separated, of finite type and of dimension zero, so
$H^q(Z,i^{-1}F)=0$ for $q>0$ and $H^0(Z,i^{-1}F)=\prod_{z\in Z}F_{\bar z}$,
a finite product, i.e. a direct sum
([lem-weil-pbc-zero-dimensional-cohomology]). Combine with Part 1.

*Part 3.* Let $\pi:C_{k'}\to C$. Each $z\in Z$ is a $k$-point, so
$Z_{k'}=Z\times_kk'$ is the finite set of $k'$-points $z\otimes k'$, and the
geometric point of $C_{k'}$ at $z\otimes k'$ maps to a geometric point over
$z$; since pullback preserves stalks,
$(F_{k'})_{\overline{z\otimes k'}}=F_{\bar z}$, and the stalks of $F_{k'}$
outside $Z_{k'}$ vanish because their images in $C$ lie outside $Z$. The
finite base change isomorphism ([lemma-weil-pbc-finite-exchange]) identifies
$\pi^{-1}i_*i^{-1}F$ with $i'_*i'^{-1}F_{k'}$ for
$i':Z_{k'}\hookrightarrow C_{k'}$. By Part 2 applied over $k$ and over $k'$,
both cohomologies vanish in positive degrees, and in degree zero the pullback
map is the identity of $\bigoplus_{z\in Z}F_{\bar z}$, since it is
compatible with the restriction maps to the stalks.
