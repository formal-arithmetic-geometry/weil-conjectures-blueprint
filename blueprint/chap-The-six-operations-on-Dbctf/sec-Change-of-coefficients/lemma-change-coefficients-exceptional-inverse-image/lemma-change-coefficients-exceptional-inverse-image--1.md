+++
id = "lemma-change-coefficients-exceptional-inverse-image--1"
kind = "lemma"
title = "Exceptional inverse image: finite ring maps"
order = 640002
aliases = ["bp-r195-1"]
lean = []
uses = ["theorem-exceptional-inverse-image", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-compact-support"]
+++
This general finite-ring comparison is bypassed by the Lean proof; the finite-coefficient passage used there is the reduction comparison in [lemma-change-coefficients-exceptional-inverse-image--2].

Assume $\Lambda=A$, $\Lambda'=B$ for a homomorphism of finite admissible rings. For $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$, the comparison

$$
\beta_{f,K}:(f^!_\Lambda K)_{\Lambda'}\longrightarrow f^!_{\Lambda'}(K_{\Lambda'})
$$

is an isomorphism in $D(X_{\mathrm{pro}\acute{e}t},\Lambda')$.
