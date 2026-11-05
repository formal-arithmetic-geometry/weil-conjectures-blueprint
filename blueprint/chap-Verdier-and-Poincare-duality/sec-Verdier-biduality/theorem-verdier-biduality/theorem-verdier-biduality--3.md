+++
id = "theorem-verdier-biduality--3"
kind = "theorem"
title = "Biduality: finite extension of $\\Ql$"
order = 844006
aliases = ["bp-r253-3"]
lean = []
uses = ["definition-constructible-sheaves", "definition-relative-dualizing-complex", "definition-verdier-dual-evaluation"]
+++
This separate coefficient stage is bypassed by the Lean proof: it passes from integral coefficients to $\overline{\mathbf Q}_\ell$ along $\mathcal O_E\to E\to\overline{\mathbf Q}_\ell$, without first proving biduality for every $E$-complex.

The intermediate assertion in the coefficient-by-coefficient argument is the following. Let $k$ have positive characteristic different from $\ell$, let $X$ be separated and of finite type over $k$, and let $E/\Ql$ be finite. For $K\in\Dctf(X_{\mathrm{pro}\acute{e}t},E)$, with dualizing complex $a_X^!E$, the morphism $\delta_K:K\to\mathbb D_X\mathbb D_XK$ is an isomorphism.
