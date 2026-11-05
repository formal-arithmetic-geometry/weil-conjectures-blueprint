+++
kind = "proof"
of = "theorem-weights-rf-shriek"
order = 1364
uses = ["proposition-weights-under-usual-operations", "lemma-weights-exact-sequence", "theorem-direct-image-mixed-sheaf"]
+++
Let $K\in D_{\le w}(X_0)$, so that each $\mathcal H^b(K)$ is mixed of
weights at most $w+b$. Applying $Rf_!$ to the ordinary truncation tower
of $K$, which is bounded and functorial, we obtain the spectral sequence

$$
E_2^{a,b}=R^af_!\mathcal H^b(K)
\ \Longrightarrow\ \mathcal H^{a+b}(Rf_!K),
$$

By naturality and the Frobenius compatibility of $Rf_!$, its
differentials and its finite abutment filtration are compatible with
the Weil structures. By Theorem [theorem-direct-image-mixed-sheaf],
$E_2^{a,b}$ is mixed of weights at most $w+a+b$, and so is its
subquotient $E_\infty^{a,b}$. The quotients of the filtration of
$\mathcal H^n(Rf_!K)$ are the $E_\infty^{a,n-a}$. By
Lemma [lemma-weights-exact-sequence] and induction on the length of
the filtration, $\mathcal H^n(Rf_!K)$ is mixed of weights at most
$w+n$. In other words, $Rf_!K\in D_{\le w}(Y_0)$. The last
assertion is the case of the structure map of $X_0$, for which the
geometric stalk of $R^nf_!K$ is $H_c^n(X,K)$ with its Frobenius
operator.
