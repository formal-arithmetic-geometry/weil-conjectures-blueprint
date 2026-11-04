+++
id = "lemma-weight-bounds-partitions"
kind = "lemma"
title = "Weight bounds and partitions"
order = 1346
lean = ["AlgebraicGeometry.HasDirectImageWeightBound.of_openClosed", "AlgebraicGeometry.HasDirectImageWeightBound.of_openClosed_target"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-weights", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $f:X_0\to Y_0$ be separated of finite type, and let $K$ be a
constructible Weil sheaf on $X_0$, mixed of weights at most $w$.

1. Let $j:U_0\to X_0$ be an open immersion with closed complement
   $i:Z_0\to X_0$. If $R^q(fj)_!j^*K$ and $R^q(fi)_!i^*K$ are mixed of
   weights at most $w+q$ for every $q$, then so is $R^qf_!K$.
2. Let $V_0\subset Y_0$ be open with closed complement $W_0$, and let
   $f_V$ and $f_W$ be the base changes of $f$ to $V_0$ and $W_0$. If
   $R^qf_{V!}(K|_{f^{-1}V_0})$ and $R^qf_{W!}(K|_{f^{-1}W_0})$ are mixed
   of weights at most $w+q$ for every $q$, then so is $R^qf_!K$.
