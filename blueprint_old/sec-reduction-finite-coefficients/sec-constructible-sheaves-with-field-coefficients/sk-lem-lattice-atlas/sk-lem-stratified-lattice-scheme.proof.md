+++
kind  = "proof"
of    = "det-lem-stratified-lattice-scheme"
+++
(1) A lisse $\cO_{E,U}$-submodule $M\subseteq E_U^r$ with $M[1/\ell]=E_U^r$ is, locally on $U$,
free with a basis which is a basis of $E_U^r$, i.e. given by a matrix in $\GL_r(E_U(U'))$ on a
cover $U'$; $E_U(U')=C(|U'|,E)$ ([det-prop-sfb-qlbar-colimit-x-invert-ell] and the description
of sections on quasi-compact objects). Two bases define the same submodule iff they differ by a
matrix in $\GL_r(\cO_{E,U}(U'))$. Hence $M$ corresponds to a continuous map
$|U'|\to\GL_r(E)/\GL_r(\cO_E)$, compatible on overlaps. Since $\GL_r(\cO_E)$ is open in
$\GL_r(E)$ (it is the preimage of an open set under the continuous entry maps, intersected
with the open condition $\det\in\cO_E^\times$), the quotient is discrete, so continuous maps to
it are locally constant: $\mathcal{L}\mathit{at}|_V$ is the constant sheaf.

(2) Choose finitely many affine $V_k$ covering $X$ on which $L$ is trivial, with transition
matrices $g_{kk'}\colon|V_k\times_XV_{k'}|\to\GL_r(E)$, continuous. For a lattice $\Lambda\subset E^r$
the stabilizer of $\Lambda$ in $\GL_r(E)$ is open (a conjugate of $\GL_r(\cO_E)$), so
$x\mapsto g_{kk'}(x)\Lambda$ is locally constant. Hence the map
$\coprod_{\Lambda}(V_k\times_XV_{k'})\to\coprod_{\Lambda}(V_k\times_XV_{k'})$ sending the copy
indexed by $\Lambda$ over the open and closed piece where $g_{kk'}\Lambda=\Lambda'$ to the copy
indexed by $\Lambda'$ is a morphism of schemes, and these maps satisfy the cocycle condition.
This is a descent datum for the schemes $T_k=\coprod_{\Lambda}V_k$ along the fpqc covering
$\coprod_kV_k\to X$. For affine $V_k=\Spec B$, $T_k\to V_k$ is ind-quasi-affine: $T_k$ is the
union of its finite subunions $\coprod_{\Lambda\in I}V_k$ ($I$ finite), which are affine open
subschemes, and every quasi-compact open of $T_k$ lies in one of them, hence is quasi-affine.
(When infinitely many lattices occur, $T_k$ is not quasi-compact, so it is not quasi-affine.)
Descent data for ind-quasi-affine morphisms along fpqc coverings are effective
([Stacks, Tag 0APK](https://stacks.math.columbia.edu/tag/0APK)); glue the results over the
finitely many affine opens of $X$. The
resulting $X$-scheme $\mathrm{Lat}(L)$ represents $\mathcal{L}\mathit{at}$ by (1) and descent of morphisms.
Being separated and étale is fpqc local on the base ([Stacks, Tag 02KU](https://stacks.math.columbia.edu/tag/02KU), [Stacks, Tag 02VN](https://stacks.math.columbia.edu/tag/02VN)), and
$T_k\to V_k$ is a disjoint union of isomorphisms, hence separated and étale. It is surjective
because $T_k\to V_k$ is (every free module has a lattice, e.g. $\cO_E^r$).

(3) On $T_k$ the copy indexed by $\Lambda$ carries the constant lattice $\Lambda_{V_k}\subseteq E^r_{V_k}$;
these are compatible with the descent datum by construction, and descend to
$M^{\mathrm{univ}}\subseteq q^*L$ by descent of module sheaves.

(4) By (2), $q\colon\mathrm{Lat}(L)\to X$ is étale and surjective, so its affine opens $W_k$ form an
étale covering of $X$. By (3), $M_k=M^{\mathrm{univ}}|_{W_k}$ is a lattice in $q^*L|_{W_k}=L|_{W_k}$.
