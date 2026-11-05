+++
id = "theorem-trace-isomorphism-top-degree--text-1"
kind = "hidden"
title = "The trace isomorphism in top degree"
order = 865001
uses = ["definition-small-pro-etale-site", "definition-weil-structure", "definition-frobenius-operator"]
+++
*Shared context.* The finite, integral and rational trace assertions retained below refer to the smooth, proper, connected $X/k$ of the theorem, with $k$ algebraically closed, and to the trace of Definition [definition-trace-map]. They are marked when the Lean route bypasses them.

The vanishing argument uses finite and profinite coefficients on a finite-type scheme over a separably closed field, and then a filtered union of compact coefficient lattices. The degree-zero and top-degree assertions used for the Weil conjectures concern $X=X_0\times_{\Fq}\Fbar$, with coefficients $\overline{\mathbf Q}_\ell$ and $\ell\ne\operatorname{char}\Fq$. Write $F$ for geometric Frobenius. The value line $\overline{\mathbf Q}_\ell(-d)$ has $F=q^d$. Each detail states its own geometric hypotheses; the top-degree isomorphisms in this route are existential and are not identified with the trace of Definition [definition-trace-map].
