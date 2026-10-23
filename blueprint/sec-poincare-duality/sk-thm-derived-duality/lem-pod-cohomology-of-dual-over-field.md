+++
id = "lem-pod-cohomology-of-dual-over-field"
kind = "lemma"
title = "Cohomology of the dual of a finite complex over a field"
lean = ["DerivedCategory.nonempty_iso_homology_ihom"]
order = 3423
uses = ["def-pod-conventions", "def-pod-perfect-point-complex", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-coefficient-point", "prop-pod-biduality-at-the-point"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), let $\Lambda\in\{E,\Qlb\}$ be one of the field coefficient rings, let $C$ be a bounded complex of finite-dimensional $\Lambda$-vector spaces, and let $C^\vee =R\operatorname {Hom}_\Lambda(C,\Lambda)$. The canonical evaluation $C\otimes _\Lambda^LC^\vee \to \Lambda$ induces perfect pairings

$$
H^i(C)\times H^{-i}(C^\vee )\longrightarrow \Lambda \qquad (i\in \mathbf Z),
$$

and the canonical comparison $C\to C^{\vee \vee }$ is an isomorphism; equivalently

$$
H^{-i}(C^\vee )\xrightarrow {\  \sim \  }H^i(C)^\vee \qquad (i\in \mathbf Z).
$$
