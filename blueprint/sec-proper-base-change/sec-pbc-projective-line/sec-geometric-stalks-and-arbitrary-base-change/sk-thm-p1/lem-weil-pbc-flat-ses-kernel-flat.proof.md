+++
kind = "proof"
of = "lem-weil-pbc-flat-ses-kernel-flat"
+++
*Criterion.* By the ideal criterion for flatness (Stacks 00HD, (4) implies (1)) it suffices to show: for every finitely generated ideal $I\subset R$ the multiplication map $\mu_{M'}:I\otimes_RM'\to M'$, $x\otimes m'\mapsto xm'$, is injective. Fix such an $I$ and write $\mu_M:I\otimes_RM\to M$ likewise.

*The diagram.* The square with top row $u:M'\to M$, bottom row $\mathrm{id}_I\otimes u:I\otimes_RM'\to I\otimes_RM$ and vertical maps $\mu_{M'}$, $\mu_M$ commutes: on generators $\mu_M((\mathrm{id}_I\otimes u)(x\otimes m'))=\mu_M(x\otimes u(m'))=x\,u(m')=u(xm')=u(\mu_{M'}(x\otimes m'))$ by $R$-linearity of $u$, and both composites are additive, so they agree on all of $I\otimes_RM'$.

*Two injective arrows.* (a) Since $M$ is flat, $\mu_M$ is injective, by the direction (1) implies (4) of the ideal criterion. (b) Since $0\to M'\to M\to M''\to0$ is exact and $M''$ is flat, $\mathrm{Tor}_1^R(M'',I)=0$ and the long exact Tor sequence (Stacks 00HL), applied with $N=I$, shows that the lower left arrow $\mathrm{id}_I\otimes u:I\otimes_RM'\to I\otimes_RM$ is injective.

*Diagram chase.* Let $z\in I\otimes_RM'$ with $\mu_{M'}(z)=0$. By the commutative square (step 2), $\mu_M((\mathrm{id}_I\otimes u)(z))=u(\mu_{M'}(z))=0$; $\mu_M$ is injective (step 3a), so $(\mathrm{id}_I\otimes u)(z)=0$; $\mathrm{id}_I\otimes u$ is injective (step 3b), so $z=0$. Hence $\mu_{M'}$ is injective for every finitely generated ideal $I$, and $M'$ is flat by step 1.
