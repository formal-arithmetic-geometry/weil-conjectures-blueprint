+++
kind = "proof"
of = "det-ambient-ind-derived-triangulated"
+++
Shifts permute cohomology sheaves, and $0\in\IndCons(X,\Lambda)$. By rotation it suffices to treat $M$
when $K,L\in\Dic(X,\Lambda)$. The long exact sequence

$$
H^n(K)\xrightarrow{\alpha}H^n(L)\to H^n(M)\to H^{n+1}(K)\xrightarrow{\beta}H^{n+1}(L)
$$

gives a short exact sequence

$$
0\to\coker\alpha\to H^n(M)\to\ker\beta\to0
$$

in $\Mod(X_{\mathrm{proét}},\Lambda)$. Since $\alpha,\beta$ are maps in $\IndCons(X,\Lambda)$, part (2) of
[sk-prop-ind-heart] gives $\coker\alpha,\ker\beta\in\IndCons(X,\Lambda)$, and closure under extensions
gives $H^n(M)\in\IndCons(X,\Lambda)$.
