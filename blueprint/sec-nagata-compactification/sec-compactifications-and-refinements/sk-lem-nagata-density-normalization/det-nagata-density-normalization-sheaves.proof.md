+++
kind  = "proof"
of    = "det-nagata-density-normalization-sheaves"
uses = ["det-nagata-density-normalization-setup", "lem-cbc-proetale-extension-zero", "lem-cbc-proetale-extension-zero-base-change", "lem-exc-proetale-closed-essential-image", "lem-exc-proetale-closed-exact", "lem-weil-extension-by-zero-exact"]
+++
All functors involved are exact on module sheaves, so it suffices to treat a
sheaf $M$ of $\Lambda_X$-modules and apply the result degreewise to a
representing complex; naturality makes the degreewise maps compatible with
the differentials. The cited sheaf-level statements are formulated for
module sheaves over a constant ring; their arguments only use the module
structure and apply verbatim to $\Lambda_X$-, $\Lambda_Z$- and
$\Lambda_{\overline X}$-module sheaves.

*Step 1: setup.* By part (2) of [det-nagata-density-normalization-setup],
$\overline X$ is qcqs, $j_V:V\hookrightarrow\overline X$ is a quasi-compact
open immersion and $i:Z\hookrightarrow\overline X$ is its closed complement.
Hence $i_*$ is exact ([lem-exc-proetale-closed-exact]), and $j_!$, $j_{Z,!}$
are exact ([lem-weil-extension-by-zero-exact]).

*Step 2: the restriction comparison.* By part (3) of
[det-nagata-density-normalization-setup], the square with sides
$j_Z:X\to Z$, $i:Z\to\overline X$, $j:X\to\overline X$ and $\mathrm{id}_X$ is
cartesian. Extension by zero commutes with base change in such a square
([lem-cbc-proetale-extension-zero-base-change]), and the base change map is
the restriction comparison; so it is an isomorphism $j_{Z,!}M\cong i^*j_!M$.

*Step 3: the restriction to $V$ vanishes.* Again by part (3),
$X\times_{\overline X}V$ is empty, so $j_V^*j_!M=0$ by the stalk description
of extension by zero ([lem-cbc-proetale-extension-zero]).

*Step 4: the pushforward comparison.* A sheaf on $\overline X$ whose
restriction to the quasi-compact open complement $V$ of $Z$ vanishes lies in
the essential image of $i_*$, and its unit $N\to i_*i^*N$ is an isomorphism
([lem-exc-proetale-closed-essential-image]). By Step 3 this applies to
$N=j_!M$. Composing with $i_*$ of the inverse of the isomorphism of Step 2
shows that the pushforward comparison $j_!M\to i_*j_{Z,!}M$ is an
isomorphism. Since $i_*$ is exact, $Ri_*=i_*$ on complexes, which gives the
assertion for $K$.
