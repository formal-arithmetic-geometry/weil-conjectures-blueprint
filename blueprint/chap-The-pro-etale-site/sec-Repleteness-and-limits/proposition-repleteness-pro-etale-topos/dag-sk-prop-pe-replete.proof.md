+++
kind = "proof"
of = "dag-sk-prop-pe-replete"
tags = ["sheaf-dag"]
uses = ["dag-det-pe-replete-definition", "dag-sk-def-pe-weak-contractible", "dag-sk-def-pe-replete"]
+++
1. Fix a scheme $X$, an inverse sequence $(F_n,t_n)$ of sheaves of sets on $X_{\mathrm{proét}}$ with epimorphic transitions, and $m\geq0$. Write $L=\varprojlim_nF_n$ and $p_m:L\to F_m$, as in [dag-det-pe-replete-definition]. For every weakly contractible object $W$, `det-pe-replete-on-contractible` applies to this same sequence and gives surjectivity of $p_m(W):L(W)\to F_m(W)$. This lemma supplies both the successive lifts above stage $m$ and their compatibility with the earlier stages; its conclusion concerns the actual sheaf limit and its projection. (uses [dag-det-pe-replete-definition], `det-pe-replete-on-contractible`)
2. Let $U$ be any object of $X_{\mathrm{proét}}$ and $y\in F_m(U)$. By `sk-thm-pe-weakly-contractible-basis`, choose a covering $\{W_i\to U\}$ by affines whose representable sheaves satisfy the splitting condition for every epimorphism onto them. By [dag-sk-def-pe-weak-contractible] these $W_i$ are weakly contractible. Step 1 therefore gives, for each $i$, a section $x_i\in L(W_i)$ with $p_m(W_i)(x_i)=y|_{W_i}$. The basis theorem applies to arbitrary $U$, so no quasi-compactness or quasi-separatedness assumption on $U$ or $X$ has been introduced. (uses [dag-sk-def-pe-weak-contractible], `sk-thm-pe-weakly-contractible-basis`)
3. The cover and sections in step 2 exhibit local surjectivity of $p_m$ for every object $U$ and every $y\in F_m(U)$. By `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective`, $p_m$ is an epimorphism. Separate local preimages suffice for this criterion: the $x_i$ need not agree on overlaps. Since the inverse sequence and $m$ were arbitrary, the defining condition of [dag-sk-def-pe-replete] holds, proving that $\Sh(X_{\mathrm{proét}})$ is replete. (uses [dag-sk-def-pe-replete], `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective`)

Proof dependencies not drawn: `det-pe-replete-on-contractible`, `sk-thm-pe-weakly-contractible-basis`, `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective`.
