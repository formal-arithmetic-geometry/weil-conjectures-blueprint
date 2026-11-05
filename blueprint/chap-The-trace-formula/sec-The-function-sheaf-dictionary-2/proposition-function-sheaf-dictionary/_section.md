+++
id = "proposition-function-sheaf-dictionary"
kind = "proposition"
title = "The function–sheaf dictionary"
order = 1029
lean = ["AlgebraicGeometry.WeilComplex.traceFunction_upperStar", "AlgebraicGeometry.WeilComplex.traceFunction_tensorLisse", "AlgebraicGeometry.WeilComplex.traceFunction_eq_add_of_distTriang"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "definition-trace-function"]
+++
Let $\Lambda$ be as in Theorem [theorem-grothendieck-lefschetz-trace-formula],
let $m\geq1$, and let $K$, $L$ be Weil complexes in $D^b_{\mathrm{ctf}}(X,\Lambda)$.

1. For $g_0:W_0\to X_0$ and $w\in W_0(\mathbf F_{q^m})$,
   $t_{g^*K,m}(w)=t_{K,m}(g_0(w))$.
2. $t_{K\otimes^{\mathbf L}_\Lambda L,m}=t_{K,m}\,t_{L,m}$.
3. For $f_0:X_0\to Y_0$ and $y\in Y_0(\mathbf F_{q^m})$,
   $t_{Rf_!K,m}(y)=\sum_{x\in X_0(\mathbf F_{q^m}),\,f_0(x)=y}t_{K,m}(x)$.
4. For $U_0\subset X_0$ open with closed complement $Z_0$, and
   $j:U\to X$, $i:Z\to X$ the inclusions,
   $t_{K,m}=t_{j_!j^*K,m}+t_{i_*i^*K,m}$, where $t_{j_!j^*K,m}$ is
   $t_{K,m}$ on $U_0(\mathbf F_{q^m})$ and $0$ on $Z_0(\mathbf F_{q^m})$.
5. $\sum_{x\in X_0(\mathbf F_{q^m})}t_{K,m}(x)
  =\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{X,K}^m\mid
  R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)$.
