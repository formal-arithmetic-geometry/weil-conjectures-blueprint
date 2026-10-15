+++
kind = "proof"
of = "det-proper-heart-continuity-cohomology"
+++
By [sk-prop-pe-hypercover] (applied to $U=Z$, with $K=M$ in degree $0$, so $a=0$) there is a hypercover
$Z_\bullet\to Z$ with each $Z_r$ affine weakly contractible, and

$$
R\Gamma(Z,M)\simeq\bigl(M(Z_0)\to M(Z_1)\to M(Z_2)\to\cdots\bigr),
$$

the alternating Čech-type cochain complex, functorially in $M$. By [det-proper-heart-continuity-sections]
each term $M\mapsto M(Z_r)$ commutes with filtered colimits and direct sums, and the differentials are
natural, so the cochain complex of $\varinjlim_iM_i$ is the filtered colimit of the cochain complexes of
the $M_i$ (and likewise for sums). Filtered colimits and direct sums of abelian groups are exact, so
they commute with cohomology of complexes. Hence $H^q(Z,\varinjlim M_i)=\varinjlim H^q(Z,M_i)$, and
similarly for sums; the identification is the natural map, by functoriality of the hypercover
computation.
