+++
id = "thm-pod-equivariance-of-the-twisted-pairing"
kind = "theorem"
title = "Equivariance of the twisted pairing"
order = 2434
uses = ["def-pod-derived-poincare-pairing", "def-pod-dual-tate-datum", "def-pur-tate-datum", "def-trf-frobenius-operators", "def-weil-frobenius-detailed", "def-weil-global-geometric-frobenius", "def-weil-weil-sheaf-complex", "lem-fix-weil-operations", "prop-pod-degree-of-the-pairing", "prop-pod-dual-tate-data-compatibility", "thm-pur-weil-equivariance-of-purity-and-trace"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), let $(K,\varphi_K)$ be a strict Weil complex with $K$ perfect. With $F_{c,K}$ and $F_{K^\vee (d)}$ the operators of [def-trf-frobenius-operators] formed from $\varphi _K$ and the datum $\varphi _{K^\vee (d)}$ of [def-pod-dual-tate-datum], the degreewise pairings satisfy

$$
\bigl\langle F_{c,K}x,\; F_{K^\vee (d)}y\bigr\rangle _i =\langle x,y\rangle _i \qquad \bigl(x\in H_c^i(X,K),\  y\in H^{2d-i}(X,K^\vee (d))\bigr),
$$

where the action on the second factor includes the scalar $q^{-d}$ on $A_X(d)$ and the pairing is the derived Poincare pairing in the form of [prop-pod-degree-of-the-pairing].
