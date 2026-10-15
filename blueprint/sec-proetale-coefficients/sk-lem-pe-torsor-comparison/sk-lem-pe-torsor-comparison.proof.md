+++
kind = "proof"
of = "sk-lem-pe-torsor-comparison"
uses = ["det-pe-torsor-comparison-affine", "det-pe-torsor-comparison-glue", "sk-prop-pe-comparison-morphism"]
+++
Write the group as $\nu_X^*G_0$ and work on an affine open of $X$
([det-pe-torsor-comparison-glue]). Using [sk-thm-pe-indetale-refinement] and
finite affine refinements, refine a trivializing covering to a single faithfully
flat ind-étale affine $U\to X$, and write $U=\varprojlim_iU_i$ with $U_i$ affine
étale over $X$. A trivialization over $U$ gives a transition element in
$\nu_X^*G_0(U\times_XU)$. By affine continuity
([sk-prop-pe-comparison-morphism]) it descends to $G_0(U_i\times_XU_i)$ for some
$i$, and the cocycle identity on the triple product holds after enlarging $i$.
Since $U\to X$ is surjective, each $U_i\to X$ is an étale covering, and gluing
the trivial torsor along this cocycle gives an étale torsor with the prescribed
pro-étale pullback ([det-pe-torsor-comparison-affine]). The same argument
descends trivializations (Stacks Project, Tag 099X).
