+++
id = "det-nagata-refinement-common-dense"
kind = "lemma"
title = "The closure of the diagonal is a common dense refinement"
uses = ["det-nagata-definition-refinement", "def-nagata-dense-compactification"]
+++
Let $S$ be qcqs, let $f:X\to S$ be separated of finite type, and let
$c_k=(X\xrightarrow{j_k}\overline X_k\xrightarrow{p_k}S)$, $k=1,2$, be
compactifications of $f$. Let $Z$ be the scheme-theoretic image of

$$
\delta=(j_1,j_2):X\longrightarrow P:=\overline X_1\times_S\overline X_2 ,
$$

with projections $q_k:Z\to\overline X_k$. Then $\delta$ factors as a
quasi-compact, scheme-theoretically dense open immersion $j:X\to Z$ followed
by the closed immersion $Z\hookrightarrow P$; the structure map $Z\to S$ is
proper, so $c=(X\xrightarrow{j}Z\to S)$ is a dense compactification; and
each $q_k$ is a refinement $c\to c_k$ in the sense of
[det-nagata-definition-refinement], i.e. $q_kj=j_k$ and
$q_k^{-1}(j_k(X))=j(X)$.

Consequently every finite nonempty family of compactifications of $f$ has a
common dense refinement.
