+++
id = "sk-lem-nagata-sketch-blowups"
kind = "lemma"
title = "Blow-ups and strict transforms"
order = 87
uses = ["sk-def-nagata-sketch-data", "sk-lem-nagata-sketch-closure"]
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isProper_blowupMap", "AlgebraicGeometry.strictTransform", "AlgebraicGeometry.IsAdmissible.exists_extend", "AlgebraicGeometry.IsAdmissible.isSchemeTheoreticallyDominant_preimage_ι"]
tags = ["sketch"]
+++
Finite-type ideal blow-ups are proper. Admissible blow-ups can be
composed, refined simultaneously, and extended from a quasi-compact open
to a qcqs ambient scheme while preserving a specified open on which they
are trivial. For $T\to X$ and $b:X'\to X$ with centre $C$, the
*strict transform* of $T$ is the scheme-theoretic closure of
$T\times_X(X\setminus C)$ in $T\times_XX'$; it is the blow-up of $T$
in the pulled-back ideal. Scheme-theoretic density of a quasi-compact preserved open
survives an admissible blow-up.
