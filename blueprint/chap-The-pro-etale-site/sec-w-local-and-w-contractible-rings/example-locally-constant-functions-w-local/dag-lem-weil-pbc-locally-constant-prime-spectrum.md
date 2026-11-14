+++
id = "dag-lem-weil-pbc-locally-constant-prime-spectrum"
kind = "dag-lemma"
title = "Prime spectrum of a locally constant function ring"
name_showing = false
order = 48501
tags = ["sheaf-dag"]
split_from = "example-locally-constant-functions-w-local--1"
dag_id = "lem-weil-pbc-locally-constant-prime-spectrum"
dag_kind = "statement"
dag_status = "unsplit"
serial = false
dag_lean = ["LocallyConstant.homeomorphPrimeSpectrum", "LocallyConstant.homeomorphPrimeSpectrum_apply", "LocallyConstant.toPrimeSpectrum", "LocallyConstant.mem_toPrimeSpectrum_asIdeal"]
+++
Use the universes of `def-weil-size-convention`. Let $S$ be a compact Hausdorff totally disconnected topological space and $R$ a commutative ring, and write $\operatorname{LC}(S,R)$ for the ring of locally constant functions $S\to R$ with pointwise operations. There is a homeomorphism $S\times\operatorname{Spec}R\xrightarrow{\sim}\operatorname{Spec}\operatorname{LC}(S,R)$ of underlying topological spaces `def-weil-affine-spectrum`, sending $(s,\mathfrak p)$ to the prime ideal $\{h:h(s)\in\mathfrak p\}$. This includes the empty space and the zero ring.

(SHEAF DAG node `lem-weil-pbc-locally-constant-prime-spectrum`; machine-alignment layer.) Split from [example-locally-constant-functions-w-local--1]. DAG kind: statement. DAG status: unsplit. Statement dependencies not drawn: `def-weil-size-convention`, `def-weil-affine-spectrum`.
