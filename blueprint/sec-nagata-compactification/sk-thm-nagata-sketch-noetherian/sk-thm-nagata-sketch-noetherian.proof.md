+++
kind  = "proof"
of    = "sk-thm-nagata-sketch-noetherian"
+++
Compactify the affine opens from [sk-lem-nagata-sketch-affine-cover].
Induct on $X_r=U_1\cup\cdots\cup U_r$. The overlap
$X_{r-1}\cap U_r$ contains the dense total intersection, so
[sk-thm-nagata-sketch-two-open] compactifies $X_r$ at each step.
The last union is $X$; the empty scheme causes no exception.
