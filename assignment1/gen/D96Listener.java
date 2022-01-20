// Generated from C:/Users/ADMIN/Documents/GitHub/HCMUT-PPL/assignment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link D96}.
 */
public interface D96Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link D96#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(D96.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(D96.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#string}.
	 * @param ctx the parse tree
	 */
	void enterString(D96.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#string}.
	 * @param ctx the parse tree
	 */
	void exitString(D96.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#string_op}.
	 * @param ctx the parse tree
	 */
	void enterString_op(D96.String_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#string_op}.
	 * @param ctx the parse tree
	 */
	void exitString_op(D96.String_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#bool_op}.
	 * @param ctx the parse tree
	 */
	void enterBool_op(D96.Bool_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#bool_op}.
	 * @param ctx the parse tree
	 */
	void exitBool_op(D96.Bool_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#relation_op}.
	 * @param ctx the parse tree
	 */
	void enterRelation_op(D96.Relation_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#relation_op}.
	 * @param ctx the parse tree
	 */
	void exitRelation_op(D96.Relation_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#int_op}.
	 * @param ctx the parse tree
	 */
	void enterInt_op(D96.Int_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#int_op}.
	 * @param ctx the parse tree
	 */
	void exitInt_op(D96.Int_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#float_op}.
	 * @param ctx the parse tree
	 */
	void enterFloat_op(D96.Float_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#float_op}.
	 * @param ctx the parse tree
	 */
	void exitFloat_op(D96.Float_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#int_gen_list}.
	 * @param ctx the parse tree
	 */
	void enterInt_gen_list(D96.Int_gen_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#int_gen_list}.
	 * @param ctx the parse tree
	 */
	void exitInt_gen_list(D96.Int_gen_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#int_gen_cm}.
	 * @param ctx the parse tree
	 */
	void enterInt_gen_cm(D96.Int_gen_cmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#int_gen_cm}.
	 * @param ctx the parse tree
	 */
	void exitInt_gen_cm(D96.Int_gen_cmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#bool_list}.
	 * @param ctx the parse tree
	 */
	void enterBool_list(D96.Bool_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#bool_list}.
	 * @param ctx the parse tree
	 */
	void exitBool_list(D96.Bool_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#bool_list_cm}.
	 * @param ctx the parse tree
	 */
	void enterBool_list_cm(D96.Bool_list_cmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#bool_list_cm}.
	 * @param ctx the parse tree
	 */
	void exitBool_list_cm(D96.Bool_list_cmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#float_list}.
	 * @param ctx the parse tree
	 */
	void enterFloat_list(D96.Float_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#float_list}.
	 * @param ctx the parse tree
	 */
	void exitFloat_list(D96.Float_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#float_list_cm}.
	 * @param ctx the parse tree
	 */
	void enterFloat_list_cm(D96.Float_list_cmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#float_list_cm}.
	 * @param ctx the parse tree
	 */
	void exitFloat_list_cm(D96.Float_list_cmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#string_list}.
	 * @param ctx the parse tree
	 */
	void enterString_list(D96.String_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#string_list}.
	 * @param ctx the parse tree
	 */
	void exitString_list(D96.String_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#string_list_cm}.
	 * @param ctx the parse tree
	 */
	void enterString_list_cm(D96.String_list_cmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#string_list_cm}.
	 * @param ctx the parse tree
	 */
	void exitString_list_cm(D96.String_list_cmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#lit}.
	 * @param ctx the parse tree
	 */
	void enterLit(D96.LitContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#lit}.
	 * @param ctx the parse tree
	 */
	void exitLit(D96.LitContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96#int_gen}.
	 * @param ctx the parse tree
	 */
	void enterInt_gen(D96.Int_genContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96#int_gen}.
	 * @param ctx the parse tree
	 */
	void exitInt_gen(D96.Int_genContext ctx);
}