+++
id = "thm-nagata-compactification"
kind = "theorem"
title = "Nagata compactification, [stacks-project]"
order = 407
lean = ["AlgebraicGeometry.NagataCompactification"]
uses = ["def-nagata-compactification", "def-nagata-final-compactification", "lemma-nagata-final-ambient-proper", "lemma-nagata-final-factorization", "lemma-nagata-final-open-immersion"]
+++
Let $S$ be quasi-compact and quasi-separated and let $f\colon X\to S$ be a
separated morphism of finite type. Then $f$ is compactifiable: the
factorization $\mathsf C_{\mathrm{Nag}}(f)$ consists of an open immersion
$j_f\colon X\to\overline X_f$ and a proper morphism
$p_f\colon\overline X_f\to S$ with $f=p_f\circ j_f$.
