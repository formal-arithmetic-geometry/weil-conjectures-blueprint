+++
kind = "proof"
of = "det-pd-biduality-field-extension"
+++
For $k'/k_0$ finite, $g$ is étale: $g^!=g^*$, and the comparisons are the
canonical adjunction comparisons for étale pullback. For an infinite extension,
such as an algebraic closure, write $k'$ as the filtered union of its finite
subextensions and apply continuity of finite-coefficient étale cohomology
([lem-weil-pbc-derived-cohomology-continuity]) on local test objects; this gives
the comparison for direct images. Closed exceptional restriction then follows
from the localization triangle $i_*i^!\to\mathrm{id}\to Rj_*j^*$, and internal
Hom by stratified dévissage of $K$.

For the dualizing objects, embed $X$ locally as $i\colon X\hookrightarrow
\mathbf A^N_{k_0}$, so that $\omega_X\simeq i^!A(N)[2N]$. Its base change is a
closed immersion $X'\hookrightarrow\mathbf A^N_{k'}$ with the same $N$, so
$g^*\omega_X\simeq\omega_{X'}$; no generic-curve $(1)[2]$ shift occurs. The
comparisons are formed from evaluation, so they identify the actual double-dual
maps ([lem-weil-duality-pairing]).
