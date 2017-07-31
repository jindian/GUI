// testDlg.h : header file
//

#if !defined(AFX_TESTDLG_H__AE18D0CB_8F9E_4E99_B3A4_0AE80C28B0BC__INCLUDED_)
#define AFX_TESTDLG_H__AE18D0CB_8F9E_4E99_B3A4_0AE80C28B0BC__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CTestDlg dialog

class CTestDlg : public CDialog
{
// Construction
public:
	CTestDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	//{{AFX_DATA(CTestDlg)
	enum { IDD = IDD_TEST_DIALOG };
		// NOTE: the ClassWizard will add data members here
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CTestDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	//{{AFX_MSG(CTestDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnButtonClicked(UINT nID);
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()

	// Calculator used function
	void DataUpdate(INT nInput);
	void OperationUpdate(UINT nID);
	void ClearCalculator();
	void UpdateResult(LONGLONG nInput);
	void DoCalculate();

private:
	LONGLONG nInputLeft;
	LONGLONG nInputRight;
	UINT nMathOp;
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_TESTDLG_H__AE18D0CB_8F9E_4E99_B3A4_0AE80C28B0BC__INCLUDED_)
