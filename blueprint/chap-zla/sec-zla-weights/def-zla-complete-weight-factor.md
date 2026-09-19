+++
id = "def-zla-complete-weight-factor"
kind = "definition"
title = "Complete weight factor"
order = 1026
uses = ["def-zla-weight-stratum", "prop-zla-weight-stratum-rational"]
+++
Continue with the hypotheses above and assume $A,B\in\mathbf Z[T]$. For
$0\leq i\leq r$ put

$$
R_i(T)=
\begin{cases}
A(T),&i\text{ odd},\\
B(T),&i\text{ even},
\end{cases}
$$

and define the *complete weight-$i$ factor* $P_i^{\mathrm{rec}}(T)$ of
the reduced fraction $A/B$ to be the weight-$i$ stratum of $R_i$ in the sense
of [def-zla-weight-stratum]. By
[prop-zla-weight-stratum-rational] it lies in $\mathbf Q[T]$, satisfies
$P_i^{\mathrm{rec}}(0)=1$, and its reciprocal roots are exactly the
reciprocal roots of $R_i$ that are universally pure of weight $i$, with the
multiplicities they have in $R_i$.
