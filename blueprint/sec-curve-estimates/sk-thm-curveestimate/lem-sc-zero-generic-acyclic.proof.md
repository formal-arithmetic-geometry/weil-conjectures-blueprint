+++
kind  = "proof"
of    = "lem-sc-zero-generic-acyclic"
+++
For a nonempty affine open $U\subseteq C$ put $F_U=\ker(u_U)$. The nonempty
affine opens form a filtered family under reverse inclusion (two of them
meet, $C$ being irreducible, and their intersection contains a nonempty
affine open), and for $U'\subseteq U$ the unit $u_{U'}$ factors through
$u_U$, so $F_U\subseteq F_{U'}$. We claim $F=\varinjlim_UF_U$. The map from
the colimit is a monomorphism, as a filtered colimit of subsheaves, and the
hypothesis says precisely that every section of $F$ lies, locally on its
domain, in the image of some $F_U$; so the map is also an epimorphism.

Fix $U$ and let $S=C\setminus U$. Since $C$ is integral of dimension at most
one and $U$ is a nonempty open, $S$ is a finite set of closed points.
Over $U$ the unit $u_U$ is an isomorphism, so $F_U$ restricts to zero on $U$.
For $i_S:S\to C$, the map $F_U\to i_{S*}i_S^*F_U$ is an
isomorphism: at a point of $S$ it is the identity, and outside
$S$ both stalks vanish. Finite direct image is exact by
[lemma-weil-pbc-finite-direct-image-exact], so its cohomology
is the cohomology on $S$. That is zero in positive degrees
by [lem-weil-pbc-zero-dimensional-cohomology], since
$S$ is a finite disjoint union of spectra of algebraically
closed fields. Hence $H^q(C,F_U)=0$ for $q>0$. Finally
[lem-weil-pbc-cohomology-filtered-colimit] identifies $H^q(C,F)$ with
$\varinjlim_UH^q(C,F_U)=0$.
