+++
kind = "proof"
of = "theorem-weights-rf-shriek"
order = 1367
uses = ["lemma-bounding-weights-mixed-sheaf", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "theorem-direct-image-mixed-sheaf"]
+++
Let $K\in D_{\le w}(X_0)$, so that each $\mathcal H^b(K)$ is [mixed](@definition-weights) of
weights at most $w+b$. Applying [$Rf_!$](@proposition-construction-independence-rf-shriek) to the ordinary truncation tower
of $K$, which is bounded and functorial, we obtain the spectral sequence

$$
E_2^{a,b}=\href{@proposition-construction-independence-rf-shriek}{R^af_!\mathcal H^b(K)}
\ \Longrightarrow\ \mathcal H^{a+b}(\href{@proposition-construction-independence-rf-shriek}{Rf_!K}),
$$

By naturality and the Frobenius compatibility of [$Rf_!$](@proposition-construction-independence-rf-shriek), its
differentials and its finite abutment filtration are compatible with
the [Weil structures](@definition-weil-structure). By Theorem [theorem-direct-image-mixed-sheaf],
$E_2^{a,b}$ is [mixed](@definition-weights) of weights at most $w+a+b$, and so is its
subquotient $E_\infty^{a,b}$. The quotients of the filtration of
$\mathcal H^n(\href{@proposition-construction-independence-rf-shriek}{Rf_!K})$ are the $E_\infty^{a,n-a}$. By
Lemma [lemma-weights-exact-sequence] and induction on the length of
the filtration, $\mathcal H^n(\href{@proposition-construction-independence-rf-shriek}{Rf_!K})$ is [mixed](@definition-weights) of weights at most
$w+n$. In other words, $\href{@proposition-construction-independence-rf-shriek}{Rf_!K}\in D_{\le w}(Y_0)$. The last
assertion is the case of the structure map of $X_0$, for which the
geometric stalk of [$R^nf_!K$](@proposition-construction-independence-rf-shriek) is $H_c^n(X,K)$ with its [Frobenius
operator](@definition-frobenius-operator).
