+++
id = "lemma-openclosed-stalk-upperstar"
kind = "lemma"
title = "Stalks of a pullback"
order = 1161
lean = ["AlgebraicGeometry.Etale.upperStarCompSheafFiberIso", "AlgebraicGeometry.Etale.upperStarCompUliftSheafFiberIso"]
uses = ["def-kun-separably-closed", "lemma-openclosed-point-ulift"]
+++
Let $f\colon Y\to X$ be a morphism of schemes, let $\bar y$ be a geometric
point of $Y$ and let $\mathcal F\in\shv{\et X}$. Then

$$
(f^*\mathcal F)_{\bar y}\cong\mathcal F_{f\circ\bar y},
$$

naturally in $\mathcal F$.
